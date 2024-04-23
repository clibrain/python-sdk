# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["KpuRunParams"]


class KpuRunParams(TypedDict, total=False):
    query: Required[str]
    """User text with the query or request to be commanded to the KPU."""

    explain_steps: bool
    """
    If true, the KPU will explain in natural language the steps of each step of each
    intent. Enabling this feature can slow down the KPU execution, and increase the
    usage metric.
    """

    retries: int
    """Number of retries in case of failure.

    Retries are sequential, and each failed intent yields a learning for the next
    intent. This feature is experimental.
    """

    file: List[FileTypes]
    """Files to be used in the KPU execution. Files can be of any type."""

    reasoner_model: Optional[
        Literal[
            "gpt-4-turbo",
            "mistral-large",
            "gpt-3.5-turbo",
            "claude-3-sonnet",
            "claude-3-opus",
            "gemini-pro",
            "azure/gpt-4-turbo",
            "openai/gpt-4-turbo",
        ]
    ]

    reasoner_prompt: Optional[str]
