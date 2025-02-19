#
# SMIRK
# Copyright (C) 2021-2022 RISE Research Institutes of Sweden AB
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from typing import List

import numpy as np
import torch

import smirk.config.paths as paths
from smirk.adas.pedestrian_detector.pedestrian_detector import (
    BoundingBox,
    PedestrianDetector,
)
from yolov5.models.common import DetectMultiBackend
from yolov5.utils.augmentations import letterbox
from yolov5.utils.general import non_max_suppression, scale_coords
from yolov5.utils.torch_utils import select_device


class YoloDetector(PedestrianDetector):
    # TODO: Store model parameters somewhere else
    NMS_IOU_THRESHOLD = 0.6
    DETECTION_THRESHOLD = 0.451

    IMG_SIZE = [640, 640]

    def __init__(self):
        self.conf = self.DETECTION_THRESHOLD
        self.device = select_device()
        self.model = DetectMultiBackend(paths.yolo_model, device=self.device)
        self.model.model.half()

        self.model.warmup(imgsz=(1, 3, *self.IMG_SIZE), half=True)

    @torch.no_grad()
    def detect_pedestrians(self, camera_frame: np.ndarray) -> List[BoundingBox]:
        # Pre-process
        im = letterbox(camera_frame, self.IMG_SIZE, stride=self.model.stride)[0]
        im = np.ascontiguousarray(im.transpose(2, 0, 1))

        im = torch.from_numpy(np.expand_dims(im, 0)).to(self.device)
        im = im.half()
        im /= 255

        # Inference
        pred = self.model(im)

        # NMS
        pred = non_max_suppression(
            pred, conf_thres=self.conf, iou_thres=self.NMS_IOU_THRESHOLD
        )[0]

        # Scale predictions to original image coordinates
        pred_boxes = (
            scale_coords(im.shape[2:], pred[:, :4], camera_frame.shape)
            .round()
            .cpu()
            .numpy()
            .astype(int)
        )

        return [self.detection_to_bounding_box(det) for det in pred_boxes]

    def detection_to_bounding_box(self, detection: np.ndarray) -> BoundingBox:
        x_min, y_min, x_max, y_max = detection

        return BoundingBox(x_min=x_min, y_min=y_min, x_max=x_max, y_max=y_max)
