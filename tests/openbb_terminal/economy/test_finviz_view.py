# IMPORTATION STANDARD


# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.core.session.current_user import (
    PreferencesModel,
    copy_user,
)
from openbb_terminal.economy import finviz_view


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("User-Agent", None)],
    }


@pytest.mark.default_cassette("test_display_valuation")
@pytest.mark.vcr
@pytest.mark.record_stdout
@pytest.mark.parametrize(
    "tab",
    [
        True,
        False,
    ],
)
def test_display_valuation(mocker, tab):
    # MOCK OBBFF
    preferences = PreferencesModel(
        USE_TABULATE_DF=tab,
        USE_ION=True,
    )
    mock_current_user = copy_user(preferences=preferences)
    mocker.patch(
        target="openbb_terminal.core.session.current_user.__current_user",
        new=mock_current_user,
    )

    # MOCK EXPORT_DATA
    mocker.patch(target="openbb_terminal.economy.finviz_view.export_data")

    finviz_view.display_valuation(
        group="sector",
        sortby="Name",
        ascend=True,
        export="",
    )


@pytest.mark.default_cassette("test_display_performance")
@pytest.mark.vcr
@pytest.mark.record_stdout
@pytest.mark.parametrize(
    "tab",
    [
        True,
        False,
    ],
)
def test_display_performance(mocker, tab):
    # MOCK OBBFF
    preferences = PreferencesModel(
        USE_TABULATE_DF=tab,
        USE_ION=True,
    )
    mock_current_user = copy_user(preferences=preferences)
    mocker.patch(
        target="openbb_terminal.core.session.current_user.__current_user",
        new=mock_current_user,
    )

    # MOCK EXPORT_DATA
    mocker.patch(target="openbb_terminal.economy.finviz_view.export_data")

    finviz_view.display_performance(
        group="sector",
        sortby="Name",
        ascend=True,
        export="",
    )


@pytest.mark.vcr(record_mode="none")
def test_display_spectrum(mocker):
    # MOCK GET_SPECTRUM_DATA
    mocker.patch(
        target="openbb_terminal.economy.finviz_view.finviz_model.get_spectrum_data"
    )

    # MOCK EXPORT_DATA
    mocker.patch(target="openbb_terminal.economy.finviz_view.export_data")

    # MOCK OPEN
    mock_image = mocker.Mock()
    mocker.patch(
        target="openbb_terminal.economy.finviz_view.Image",
        new=mock_image,
    )

    finviz_view.display_spectrum(
        group="sector",
        export="jpg",
    )

    mock_image.open().show.assert_called_once()


@pytest.mark.default_cassette("test_display_future")
@pytest.mark.vcr
@pytest.mark.record_stdout
@pytest.mark.parametrize(
    "tab",
    [
        True,
        False,
    ],
)
def test_display_future(mocker, tab):
    # MOCK OBBFF
    preferences = PreferencesModel(
        USE_TABULATE_DF=tab,
        USE_ION=True,
    )
    mock_current_user = copy_user(preferences=preferences)
    mocker.patch(
        target="openbb_terminal.core.session.current_user.__current_user",
        new=mock_current_user,
    )

    # MOCK EXPORT_DATA
    mocker.patch(target="openbb_terminal.economy.finviz_view.export_data")

    finviz_view.display_future(
        future_type="Indices",
        sortby="ticker",
        ascend=False,
        export="",
    )
