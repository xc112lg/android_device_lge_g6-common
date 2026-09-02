#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

# g6-common's own proprietary-files.txt (biometrics, light, audio configs,
# etc.) doesn't need any of msm8996-common's blob_fixup()/replace_needed
# patches, so this stays empty for now -- same as how a real leaf device
# (e.g. android_device_samsung_a71) doesn't re-import a71-common's
# blob_fixups either. Each tier only fixes up blobs it actually lists.
module = ExtractUtilsModule(
    'g6-common',
    'lge',
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(module, 'msm8996-common', 'lge')
    utils.run()
