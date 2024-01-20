'''
Author: 王泽洲 leon.kepler@bytedance.com
Date: 2024-01-19 16:47:02
LastEditors: 王泽洲 leon.kepler@bytedance.com
LastEditTime: 2024-01-19 22:00:40
FilePath: /uniflow/uniflow/op/basic/expand_op.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""Linear operation."""
import copy
from typing import Any, Mapping, Sequence
from uniflow.node import Node
from uniflow.op.op import Op
import uniflow.op.utils as utils


class ExpandOp(Op):
    """Linear operation class."""
    def __init__(self, name: str, split_func = "half_split") -> None:
        """Constructor of op class for uniflow.

        Args:
            name (str): Name of the op.
        """
        self._scope_name = utils.get_op_scope_name(name)
        self._count = 0
        if split_func == "half_split":
            self.split_func = self.half_split

    def _transform(self, value_dict: Mapping[str, Any]) -> Mapping[str, Any]:
        """Transform value dict.

        Args:
            value_dict (Mapping[str, Any]): Input value dict.

        Returns:
            Mapping[str, Any]: Output value dict.
        """
        return copy.deepcopy(value_dict)

    def __call__(self, nodes: Sequence[Node]) -> Sequence[Node]:
        """Call linear operation.

        Args:
            nodes (Sequence[Node]): Input nodes.

        Returns:
            Sequence[Node]: Output nodes.
        """
        output_nodes = []
        for node in nodes:
            value_dict = self._transform(node.value_dict)
            value_dicts = self.split_func(value_dict)
            
            for v in value_dicts:
                output_nodes.append(
                    Node(name=self.unique_name(), value_dict=v, prev_nodes=[node])
                )
        return output_nodes
    
    def half_split(self, value_dict: Mapping[str, Any]) :
        # 将前n//2 放入一个 Node，后面的放入一个 Node
        n = len(value_dict)   # dict个数
        # 对每一个dict进行划分，前n//2个放入一个dict，后面的放入一个dict
        for i in range(n):
            first_half = {}
            second_half = {}
            m = len(value_dict[i])  # dict中的key个数
            for j, key in enumerate(value_dict[i].keys()):
                if j < m//2:
                    first_half[key] = value_dict[i][key]
                else:
                    second_half[key] = value_dict[i][key]
        value_dicts = []
        value_dicts.append(first_half)
        value_dicts.append(second_half)
        return value_dicts
