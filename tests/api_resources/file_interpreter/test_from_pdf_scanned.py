# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from maisa import Maisa, AsyncMaisa
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFromPdfScanned:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Maisa) -> None:
        from_pdf_scanned = client.file_interpreter.from_pdf_scanned.create(
            file=b"raw file contents",
        )
        assert_matches_type(object, from_pdf_scanned, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Maisa) -> None:
        from_pdf_scanned = client.file_interpreter.from_pdf_scanned.create(
            file=b"raw file contents",
            lang="en",
            max_pages=0,
            variable1_description="The name of the person.",
            variable1_name="Name",
            variable1_type="string",
            variable2_description="The name of the person.",
            variable2_name="Name",
            variable2_type="string",
            variable3_description="The name of the person.",
            variable3_name="Name",
            variable3_type="string",
            variable4_description="The name of the person.",
            variable4_name="Name",
            variable4_type="string",
        )
        assert_matches_type(object, from_pdf_scanned, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Maisa) -> None:
        response = client.file_interpreter.from_pdf_scanned.with_raw_response.create(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        from_pdf_scanned = response.parse()
        assert_matches_type(object, from_pdf_scanned, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Maisa) -> None:
        with client.file_interpreter.from_pdf_scanned.with_streaming_response.create(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            from_pdf_scanned = response.parse()
            assert_matches_type(object, from_pdf_scanned, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFromPdfScanned:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMaisa) -> None:
        from_pdf_scanned = await async_client.file_interpreter.from_pdf_scanned.create(
            file=b"raw file contents",
        )
        assert_matches_type(object, from_pdf_scanned, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMaisa) -> None:
        from_pdf_scanned = await async_client.file_interpreter.from_pdf_scanned.create(
            file=b"raw file contents",
            lang="en",
            max_pages=0,
            variable1_description="The name of the person.",
            variable1_name="Name",
            variable1_type="string",
            variable2_description="The name of the person.",
            variable2_name="Name",
            variable2_type="string",
            variable3_description="The name of the person.",
            variable3_name="Name",
            variable3_type="string",
            variable4_description="The name of the person.",
            variable4_name="Name",
            variable4_type="string",
        )
        assert_matches_type(object, from_pdf_scanned, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMaisa) -> None:
        response = await async_client.file_interpreter.from_pdf_scanned.with_raw_response.create(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        from_pdf_scanned = await response.parse()
        assert_matches_type(object, from_pdf_scanned, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMaisa) -> None:
        async with async_client.file_interpreter.from_pdf_scanned.with_streaming_response.create(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            from_pdf_scanned = await response.parse()
            assert_matches_type(object, from_pdf_scanned, path=["response"])

        assert cast(Any, response.is_closed) is True
