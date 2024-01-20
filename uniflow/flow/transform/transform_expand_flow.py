'''
Author: 王泽洲 leon.kepler@bytedance.com
Date: 2024-01-19 19:57:39
LastEditors: 王泽洲 leon.kepler@bytedance.com
LastEditTime: 2024-01-19 21:06:54
FilePath: /uniflow/uniflow/flow/transform/transform_expand_flow.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""Flow class."""
from typing import Any, Dict, Sequence

from uniflow.constants import TRANSFORM
from uniflow.flow.flow import Flow
from uniflow.node import Node
from uniflow.op.basic.expand_op import ExpandOp
from uniflow.op.prompt import PromptTemplate
from typing import Any, Mapping, Sequence

class TransformExpandFlow(Flow):
    """Copy flow class.

    This is a demo flow does nothing but copy the input nodes.
    """

    TAG = TRANSFORM

    def __init__(
        self,
        prompt_template: PromptTemplate,
        model_config: Dict[str, Any],
        split_func
    ) -> None:  # pylint: disable=useless-parent-delegation
        """Initialize ExpandFlow class."""
        
        self._expand_op = ExpandOp(name="expand_op", split_func="half_split")
        super().__init__()

    def run(self, nodes: Sequence[Node]) -> Sequence[Node]:
        """Run ExpandFlow.

        Args:
            nodes (Sequence[Node]): Nodes to run.

        Returns:
            Sequence[Node]: Nodes after running.
        """
        return self._expand_op(nodes)

