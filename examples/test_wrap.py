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

inspector = Inspector()

@inspector.wrap
def child(x):
    with inspector.phase("squared"):
        return x * x

@inspector.wrap
def parent():
    with inspector.phase("setup"):
        a = child(3)
    return a + 1

if __name__ == "__main__":
    result, trace = inspector.inspect(parent)
    trace.save("examples/wrapped_trace.json")
    print("OK")
