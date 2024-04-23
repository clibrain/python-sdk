# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ..._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from ...types.file_interpreter import from_pdf_scanned_create_params

__all__ = ["FromPdfScanned", "AsyncFromPdfScanned"]


class FromPdfScanned(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FromPdfScannedWithRawResponse:
        return FromPdfScannedWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FromPdfScannedWithStreamingResponse:
        return FromPdfScannedWithStreamingResponse(self)

    def create(
        self,
        *,
        file: FileTypes,
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | NotGiven = NOT_GIVEN,
        max_pages: int | NotGiven = NOT_GIVEN,
        variable1_description: str | NotGiven = NOT_GIVEN,
        variable1_name: str | NotGiven = NOT_GIVEN,
        variable1_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        variable2_description: str | NotGiven = NOT_GIVEN,
        variable2_name: str | NotGiven = NOT_GIVEN,
        variable2_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        variable3_description: str | NotGiven = NOT_GIVEN,
        variable3_name: str | NotGiven = NOT_GIVEN,
        variable3_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        variable4_description: str | NotGiven = NOT_GIVEN,
        variable4_name: str | NotGiven = NOT_GIVEN,
        variable4_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Interprets pdf file and returns some extracted variables.

        Args:
          lang: The language of the output. If not provided, the language used will be the same
              as the language of the text provided.

          max_pages: The maximum number of pages to be extracted.

          variable1_description: The description of the variable.

          variable1_name: The name of the variable to be extracted.

          variable1_type: Text Extraction Request Variable Type.

          variable2_description: The description of the variable.

          variable2_name: The name of the variable to be extracted.

          variable2_type: Text Extraction Request Variable Type.

          variable3_description: The description of the variable.

          variable3_name: The name of the variable to be extracted.

          variable3_type: Text Extraction Request Variable Type.

          variable4_description: The description of the variable.

          variable4_name: The name of the variable to be extracted.

          variable4_type: Text Extraction Request Variable Type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "lang": lang,
                "max_pages": max_pages,
                "variable1_description": variable1_description,
                "variable1_name": variable1_name,
                "variable1_type": variable1_type,
                "variable2_description": variable2_description,
                "variable2_name": variable2_name,
                "variable2_type": variable2_type,
                "variable3_description": variable3_description,
                "variable3_name": variable3_name,
                "variable3_type": variable3_type,
                "variable4_description": variable4_description,
                "variable4_name": variable4_name,
                "variable4_type": variable4_type,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/file-interpreter/from-pdf-scanned",
            body=maybe_transform(body, from_pdf_scanned_create_params.FromPdfScannedCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncFromPdfScanned(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFromPdfScannedWithRawResponse:
        return AsyncFromPdfScannedWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFromPdfScannedWithStreamingResponse:
        return AsyncFromPdfScannedWithStreamingResponse(self)

    async def create(
        self,
        *,
        file: FileTypes,
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | NotGiven = NOT_GIVEN,
        max_pages: int | NotGiven = NOT_GIVEN,
        variable1_description: str | NotGiven = NOT_GIVEN,
        variable1_name: str | NotGiven = NOT_GIVEN,
        variable1_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        variable2_description: str | NotGiven = NOT_GIVEN,
        variable2_name: str | NotGiven = NOT_GIVEN,
        variable2_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        variable3_description: str | NotGiven = NOT_GIVEN,
        variable3_name: str | NotGiven = NOT_GIVEN,
        variable3_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        variable4_description: str | NotGiven = NOT_GIVEN,
        variable4_name: str | NotGiven = NOT_GIVEN,
        variable4_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Interprets pdf file and returns some extracted variables.

        Args:
          lang: The language of the output. If not provided, the language used will be the same
              as the language of the text provided.

          max_pages: The maximum number of pages to be extracted.

          variable1_description: The description of the variable.

          variable1_name: The name of the variable to be extracted.

          variable1_type: Text Extraction Request Variable Type.

          variable2_description: The description of the variable.

          variable2_name: The name of the variable to be extracted.

          variable2_type: Text Extraction Request Variable Type.

          variable3_description: The description of the variable.

          variable3_name: The name of the variable to be extracted.

          variable3_type: Text Extraction Request Variable Type.

          variable4_description: The description of the variable.

          variable4_name: The name of the variable to be extracted.

          variable4_type: Text Extraction Request Variable Type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "lang": lang,
                "max_pages": max_pages,
                "variable1_description": variable1_description,
                "variable1_name": variable1_name,
                "variable1_type": variable1_type,
                "variable2_description": variable2_description,
                "variable2_name": variable2_name,
                "variable2_type": variable2_type,
                "variable3_description": variable3_description,
                "variable3_name": variable3_name,
                "variable3_type": variable3_type,
                "variable4_description": variable4_description,
                "variable4_name": variable4_name,
                "variable4_type": variable4_type,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/file-interpreter/from-pdf-scanned",
            body=await async_maybe_transform(body, from_pdf_scanned_create_params.FromPdfScannedCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class FromPdfScannedWithRawResponse:
    def __init__(self, from_pdf_scanned: FromPdfScanned) -> None:
        self._from_pdf_scanned = from_pdf_scanned

        self.create = to_raw_response_wrapper(
            from_pdf_scanned.create,
        )


class AsyncFromPdfScannedWithRawResponse:
    def __init__(self, from_pdf_scanned: AsyncFromPdfScanned) -> None:
        self._from_pdf_scanned = from_pdf_scanned

        self.create = async_to_raw_response_wrapper(
            from_pdf_scanned.create,
        )


class FromPdfScannedWithStreamingResponse:
    def __init__(self, from_pdf_scanned: FromPdfScanned) -> None:
        self._from_pdf_scanned = from_pdf_scanned

        self.create = to_streamed_response_wrapper(
            from_pdf_scanned.create,
        )


class AsyncFromPdfScannedWithStreamingResponse:
    def __init__(self, from_pdf_scanned: AsyncFromPdfScanned) -> None:
        self._from_pdf_scanned = from_pdf_scanned

        self.create = async_to_streamed_response_wrapper(
            from_pdf_scanned.create,
        )
