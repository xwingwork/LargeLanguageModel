# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
from pathlib import Path


def get_project_root() -> str:
    """Get the absolute path to the project root directory."""
    # When running as a script, __file__ will be the actual file path
    # This works whether running from src/scripts or from project root
    current_file = Path(__file__).resolve()
    return str(current_file.parent.parent.parent)


def validate_path(
    path: str,
    is_input: bool = True,
    data_dir: str | None = None,
    create_dirs: bool = True,
) -> str:
    """
    Validate and resolve a file path to ensure it's safe.

    Args:
        path: The path to validate
        is_input: Whether this is an input file (True) or output file (False)
        data_dir: Optional specific data directory to use for relative paths
        create_dirs: Whether to create directories for output files (default: True)

    Returns:
        str: The validated absolute path

    Raises:
        ValueError: If the path is outside the project directory
        FileNotFoundError: If an input file doesn't exist
    """
    try:
        project_root = get_project_root()

        # If path is not absolute and data_dir is specified, make it relative to data_dir
        if not os.path.isabs(path) and data_dir:
            path = os.path.join(project_root, data_dir, path)

        # Convert to absolute path and resolve any symlinks
        abs_path = os.path.abspath(os.path.realpath(path))

        # Check if the path is within the project directory
        if not abs_path.startswith(project_root):
            raise ValueError(f"Path must be within the project directory: {project_root}")

        if is_input:
            # For input files, check that they exist
            if not os.path.isfile(abs_path):
                raise FileNotFoundError(f"Input file not found: {abs_path}")
        elif create_dirs:
            # For output files, ensure the directory exists if create_dirs is True
            os.makedirs(os.path.dirname(abs_path), exist_ok=True)

        return abs_path
    except Exception as e:
        print(f"Error validating path: {e}", file=sys.stderr)
        sys.exit(1)
