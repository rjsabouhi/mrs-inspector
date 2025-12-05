# Copyright 2025 RJ Sabouhi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from mrs_inspector import Inspector
from mrs_inspector.tracer import Trace


def compute():
    return 42


if __name__ == "__main__":
    inspector = Inspector()
    result, trace = inspector.inspect(compute)

    trace.save_json("examples/load_test.json")

    loaded = Trace.load_json("examples/load_test.json")

    print("OK — Loaded trace length:", len(loaded.states))

