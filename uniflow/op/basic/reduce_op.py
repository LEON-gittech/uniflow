'''
Author: 王泽洲 leon.kepler@bytedance.com
Date: 2024-01-19 16:47:02
LastEditors: 王泽洲 leon.kepler@bytedance.com
LastEditTime: 2024-01-19 22:09:55
FilePath: /uniflow/uniflow/op/basic/expand_op.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""Linear operation."""
import copy
from typing import Any, Mapping, Sequence
from uniflow.node import Node
from uniflow.op.op import Op
import uniflow.op.utils as utils


class ReduceOp(Op):
    """Linear operation class."""
    def __init__(self, name: str, merge_func = "half_merge") -> None:
        """Constructor of op class for uniflow.

        Args:
            name (str): Name of the op.
        """
        self._scope_name = utils.get_op_scope_name(name)
        self._count = 0
        if merge_func == "half_merge":
            self.merge_func = self.half_merge

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

        value_dicts = []
        for node in nodes:
            v = self._transform(node.value_dict)
            value_dicts.append(v)
            
        value_dict = self.merge_func(value_dicts)
        output_node = Node(name=self.unique_name(), value_dict=value_dict, prev_nodes=nodes)
        
        return [output_node]
    
    def half_merge(self, value_dicts) :
        value_dict = {}
        n = len(value_dicts)
        n_k = len(value_dicts[0].keys())
        for i in range(n_k):
            keys = ""
            values = ""
            for j in range(n):
                if j==0:
                    keys += list(value_dicts[j].keys())[i]
                    values += str(list(value_dicts[j].values())[i])
                else:
                    keys += " " + list(value_dicts[j].keys())[i]
                    values += " " + str(list(value_dicts[j].values())[i])
            value_dict[keys] = values
        return value_dict
