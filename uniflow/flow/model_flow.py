"""Model Flow Module."""
from typing import Any, Dict, Sequence

from uniflow.flow.flow import Flow
from uniflow.model.config import ModelConfig
from uniflow.model.model import JsonModel, Model, OpenAIJsonModel
from uniflow.node.node import Node
from uniflow.op.model.model_op import ModelOp

FEW_SHOT_TEMPLATE = {}


class ModelFlow(Flow):
    """Model Flow Class."""

    MODEL_NAME: str = "OpenAIModelServer"
    MODEL_CONFIG: ModelConfig = ModelConfig
    FEW_SHOT_TEMPLATE: Dict[str, Any] = FEW_SHOT_TEMPLATE

    def __init__(self) -> None:
        """Model Flow Constructor."""
        super().__init__()
        self._model_op = ModelOp(
            name="model_op",
            model=JsonModel(
                model_name=self.MODEL_NAME,
                model_config=self.MODEL_CONFIG(),
                few_shot_template=self.FEW_SHOT_TEMPLATE,
            ),
        )

    def run(self, nodes: Sequence[Node]) -> Sequence[Node]:
        """Run Model Flow.

        Args:
            nodes (Sequence[Node]): Nodes to run.

        Returns:
            Sequence[Node]: Nodes after running.
        """
        return self._model_op(nodes)


class OpenAIJsonModelFlow(Flow):
    """OpenAI Json Model Flow Class."""

    MODEL_NAME: str = "OpenAIModelServer"
    MODEL_CONFIG: ModelConfig = ModelConfig
    FEW_SHOT_TEMPLATE: Dict[str, Any] = FEW_SHOT_TEMPLATE

    def __init__(self) -> None:
        """OpenAI Json Model Flow Constructor."""
        super().__init__()
        self._model_op = ModelOp(
            name="openai_json_model_op",
            model=OpenAIJsonModel(
                model_name=self.MODEL_NAME,
                model_config=self.MODEL_CONFIG(response_format={"type": "json_object"}),
                few_shot_template=self.FEW_SHOT_TEMPLATE,
            ),
        )

    def run(self, nodes: Sequence[Node]) -> Sequence[Node]:
        """Run Model Flow.

        Args:
            nodes (Sequence[Node]): Nodes to run.

        Returns:
            Sequence[Node]: Nodes after running.
        """
        return self._model_op(nodes)


class HuggingFaceModelFlow(Flow):
    """HuggingFace Model Flow Class."""

    MODEL_NAME: str = "HuggingfaceModelServer"
    MODEL_CONFIG: ModelConfig = ModelConfig
    FEW_SHOT_TEMPLATE: Dict[str, Any] = FEW_SHOT_TEMPLATE

    def __init__(self) -> None:
        """HuggingFace Model Flow Constructor."""
        super().__init__()
        self._model_op = ModelOp(
            name="huggingface_model_op",
            model=Model(
                model_name=self.MODEL_NAME,
                model_config=self.MODEL_CONFIG(
                    model_name="mistralai/Mistral-7B-Instruct-v0.1"
                ),
                few_shot_template=self.FEW_SHOT_TEMPLATE,
            ),
        )

    def run(self, nodes: Sequence[Node]) -> Sequence[Node]:
        """Run Model Flow.

        Args:
            nodes (Sequence[Node]): Nodes to run.

        Returns:
            Sequence[Node]: Nodes after running.
        """
        return self._model_op(nodes)


class LMQGModelFlow(Flow):
    """LMQG Model Flow Class."""

    MODEL_NAME: str = "LMQGModelServer"
    MODEL_CONFIG: ModelConfig = ModelConfig
    FEW_SHOT_TEMPLATE: Dict[str, Any] = FEW_SHOT_TEMPLATE

    def __init__(self) -> None:
        """HuggingFace Model Flow Constructor."""
        super().__init__()
        self._model_op = ModelOp(
            name="lmqg_model_op",
            model=Model(
                model_name=self.MODEL_NAME,
                model_config=self.MODEL_CONFIG(model_name="lmqg/t5-base-squad-qg-ae"),
                few_shot_template=self.FEW_SHOT_TEMPLATE,
            ),
        )

    def run(self, nodes: Sequence[Node]) -> Sequence[Node]:
        """Run Model Flow.

        Args:
            nodes (Sequence[Node]): Nodes to run.

        Returns:
            Sequence[Node]: Nodes after running.
        """
        return self._model_op(nodes)