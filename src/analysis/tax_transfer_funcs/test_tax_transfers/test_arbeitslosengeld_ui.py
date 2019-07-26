import pandas as pd
import pytest
from pandas.testing import assert_series_equal

from src.analysis.tax_transfer_funcs.arbeitslosengeld import ui
from src.analysis.tax_transfer_funcs.taxes import tarif
from src.analysis.tax_transfer_funcs.test_tax_transfers.auxiliary_test_tax import (
    load_input,
)
from src.analysis.tax_transfer_funcs.test_tax_transfers.auxiliary_test_tax import (
    load_output,
)
from src.analysis.tax_transfer_funcs.test_tax_transfers.auxiliary_test_tax import (
    load_tb,
)

input_cols = [
    "pid",
    "hid",
    "tu_id",
    "m_wage_l1",
    "east",
    "child",
    "months_ue",
    "months_ue_l1",
    "months_ue_l2",
    "alg_soep",
    "m_pensions",
    "w_hours",
    "child_num_tu",
    "age",
    "year",
]

years = [2010, 2011, 2015, 2019]


@pytest.mark.parametrize("year", years)
def test_ui(year):
    file_name = "test_dfs_ui.xlsx"
    df = load_input(year, file_name, input_cols, pd_kwargs={"true_values": "TRUE"})
    tb = load_tb(year)
    tb["yr"] = year
    tb["tax_schedule"] = tarif
    expected = load_output(year, file_name, "m_alg1")
    calculated = pd.Series(name="m_alg1")
    for pid in df["pid"].unique():
        calculated = calculated.append(ui(df[df["pid"] == pid], tb))
    assert_series_equal(calculated, expected, check_less_precise=3)
