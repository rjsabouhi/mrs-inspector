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
from mrs_inspector.graph import GraphBuilder


def main():
    return "ready"


if __name__ == "__main__":
    inspector = Inspector()
    result, trace = inspector.inspect(main)

    trace.save("examples/trace.json")

    gb = GraphBuilder()
    g = gb.build(trace)
    gb.save_png("examples/graph.png")

    print("Trace written to examples/trace.json")
    print("Graph written to examples/graph.png")
