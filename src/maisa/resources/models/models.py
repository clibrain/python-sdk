# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .embeddings import (
    Embeddings,
    AsyncEmbeddings,
    EmbeddingsWithRawResponse,
    AsyncEmbeddingsWithRawResponse,
    EmbeddingsWithStreamingResponse,
    AsyncEmbeddingsWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Models", "AsyncModels"]


class Models(SyncAPIResource):
    @cached_property
    def embeddings(self) -> Embeddings:
        return Embeddings(self._client)

    @cached_property
    def with_raw_response(self) -> ModelsWithRawResponse:
        return ModelsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelsWithStreamingResponse:
        return ModelsWithStreamingResponse(self)


class AsyncModels(AsyncAPIResource):
    @cached_property
    def embeddings(self) -> AsyncEmbeddings:
        return AsyncEmbeddings(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncModelsWithRawResponse:
        return AsyncModelsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelsWithStreamingResponse:
        return AsyncModelsWithStreamingResponse(self)


class ModelsWithRawResponse:
    def __init__(self, models: Models) -> None:
        self._models = models

    @cached_property
    def embeddings(self) -> EmbeddingsWithRawResponse:
        return EmbeddingsWithRawResponse(self._models.embeddings)


class AsyncModelsWithRawResponse:
    def __init__(self, models: AsyncModels) -> None:
        self._models = models

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsWithRawResponse:
        return AsyncEmbeddingsWithRawResponse(self._models.embeddings)


class ModelsWithStreamingResponse:
    def __init__(self, models: Models) -> None:
        self._models = models

    @cached_property
    def embeddings(self) -> EmbeddingsWithStreamingResponse:
        return EmbeddingsWithStreamingResponse(self._models.embeddings)


class AsyncModelsWithStreamingResponse:
    def __init__(self, models: AsyncModels) -> None:
        self._models = models

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsWithStreamingResponse:
        return AsyncEmbeddingsWithStreamingResponse(self._models.embeddings)
