"""Contribution rate for health insurance."""

from _gettsim.shared import policy_info


@policy_info(
    end_date="2005-06-30",
)
def ges_krankenv_beitr_satz_arbeitnehmer(
    sozialv_beitr_params: dict,
) -> float:
    """Employee's health insurance contribution rate until June 2005.

    Basic split between employees and employers.

    Parameters
    ----------
    sozialv_beitr_params
        See params documentation :ref:`sozialv_beitr_params <sozialv_beitr_params>`.

    Returns
    -------
    Beitragssatz for statutory health insurance.

    """

    return sozialv_beitr_params["beitr_satz"]["ges_krankenv"]["mean_allgemein"] / 2


@policy_info(
    end_date="2005-06-30",
)
def _ges_krankenv_beitr_satz_arbeitnehmer_jahresanfang(
    sozialv_beitr_params: dict,
) -> float:
    """Employee's health insurance contribution rate for the beginning of the year until
    June 2005.

    Basic split between employees and employers.

    Parameters
    ----------
    sozialv_beitr_params
        See params documentation :ref:`sozialv_beitr_params <sozialv_beitr_params>`.

    Returns
    -------
    Beitragssatz for statutory health insurance at the begging of the year.

    """
    return (
        sozialv_beitr_params["beitr_satz_jahresanfang"]["ges_krankenv"][
            "mean_allgemein"
        ]
        / 2
    )


@policy_info(
    start_date="2005-07-01",
    end_date="2008-12-31",
    name_in_dag="ges_krankenv_beitr_satz_arbeitnehmer",
)
def ges_krankenv_beitr_satz_mean_kassenspezifisch_zusatzbeitrag_nur_arbeitnehmer(
    ges_krankenv_zusatzbeitr_satz: float,
    sozialv_beitr_params: dict,
) -> float:
    """Employee's health insurance contribution rate.

    From July 2005 until December 2008. The contribution rates consists of a general
    rate (split equally between employers and employees, differs across sickness funds)
    and a top-up rate, which is fully paid by employees.

    Parameters
    ----------
    ges_krankenv_zusatzbeitr_satz
        See :func:`ges_krankenv_zusatzbeitr_satz`.
    sozialv_beitr_params
        See params documentation :ref:`sozialv_beitr_params <sozialv_beitr_params>`.

    Returns
    -------
    Beitragssatz for statutory health insurance.

    """

    mean_allgemein = sozialv_beitr_params["beitr_satz"]["ges_krankenv"][
        "mean_allgemein"
    ]

    return mean_allgemein / 2 + ges_krankenv_zusatzbeitr_satz


@policy_info(
    start_date="2005-07-01",
    end_date="2008-12-31",
    name_in_dag="_ges_krankenv_beitr_satz_arbeitnehmer_jahresanfang",
)
def ges_krankenv_beitr_satz_mean_kassenspezifisch_zusatzbeitrag_nur_arbeitnehmer_jahresanfang(  # noqa: E501
    ges_krankenv_zusatzbeitr_satz: float,
    sozialv_beitr_params: dict,
) -> float:
    """Employee's health insurance contribution rate at the beginning of the year.

    From July 2005 until December 2008. The contribution rates consists of a general
    rate (split equally between employers and employees, differs across sickness funds)
    and a top-up rate, which is fully paid by employees.

    Parameters
    ----------
    ges_krankenv_zusatzbeitr_satz
        See :func:`ges_krankenv_zusatzbeitr_satz`.
    sozialv_beitr_params
        See params documentation :ref:`sozialv_beitr_params <sozialv_beitr_params>`.

    Returns
    -------
    Beitragssatz for statutory health insurance at the beginning of the year.

    """

    mean_allgemein = sozialv_beitr_params["beitr_satz_jahresanfang"]["ges_krankenv"][
        "mean_allgemein"
    ]

    return mean_allgemein / 2 + ges_krankenv_zusatzbeitr_satz


@policy_info(
    start_date="2009-01-01",
    end_date="2018-12-31",
    name_in_dag="ges_krankenv_beitr_satz_arbeitnehmer",
)
def ges_krankenv_beitr_satz_einheitlich_zusatzbeitrag_nur_arbeitnehmer(
    ges_krankenv_zusatzbeitr_satz: float,
    sozialv_beitr_params: dict,
) -> float:
    """Employee's health insurance contribution rate.

    From January 2009 until December 2018. The contribution rates consists of a general
    rate (split equally between employers and employees, same for all sickness funds)
    and a top-up rate, which is fully paid by employees.

    Parameters
    ----------
    ges_krankenv_zusatzbeitr_satz
        See :func:`ges_krankenv_zusatzbeitr_satz`.
    sozialv_beitr_params
        See params documentation :ref:`sozialv_beitr_params <sozialv_beitr_params>`.

    Returns
    -------
    Beitragssatz for statutory health insurance.

    """

    allgemein = sozialv_beitr_params["beitr_satz"]["ges_krankenv"]["allgemein"]

    return allgemein / 2 + ges_krankenv_zusatzbeitr_satz


@policy_info(
    start_date="2009-01-01",
    end_date="2018-12-31",
    name_in_dag="_ges_krankenv_beitr_satz_arbeitnehmer_jahresanfang",
)
def ges_krankenv_beitr_satz_einheitlich_zusatzbeitrag_nur_arbeitnehmer_jahresanfang(
    ges_krankenv_zusatzbeitr_satz: float,
    sozialv_beitr_params: dict,
) -> float:
    """Employee's health insurance contribution rate at the beginning of the year.

    From January 2009 until December 2018. The contribution rates consists of a general
    rate (split equally between employers and employees, same for all sickness funds)
    and a top-up rate, which is fully paid by employees.

    Parameters
    ----------
    ges_krankenv_zusatzbeitr_satz
        See :func:`ges_krankenv_zusatzbeitr_satz`.
    sozialv_beitr_params
        See params documentation :ref:`sozialv_beitr_params <sozialv_beitr_params>`.

    Returns
    -------
    Beitragssatz for statutory health insurance at the beginning of the year.

    """

    allgemein = sozialv_beitr_params["beitr_satz_jahresanfang"]["ges_krankenv"][
        "allgemein"
    ]

    return allgemein / 2 + ges_krankenv_zusatzbeitr_satz


@policy_info(
    start_date="2019-01-01",
    name_in_dag="ges_krankenv_beitr_satz_arbeitnehmer",
)
def ges_krankenv_beitr_satz_zusatzbeitrag_arbeitnehmer_paritätisch(
    ges_krankenv_zusatzbeitr_satz: float,
    sozialv_beitr_params: dict,
) -> float:
    """Employee's health insurance contribution rate.

    Since 2019. Zusatzbeitrag is split equally between employers and employees.

    Parameters
    ----------
    sozialv_beitr_params
        See params documentation :ref:`sozialv_beitr_params <sozialv_beitr_params>`.

    Returns
    -------

    """
    allgemeiner_beitr_satz = sozialv_beitr_params["beitr_satz"]["ges_krankenv"][
        "allgemein"
    ]
    return (allgemeiner_beitr_satz + ges_krankenv_zusatzbeitr_satz) / 2


@policy_info(
    start_date="2019-01-01",
    name_in_dag="_ges_krankenv_beitr_satz_arbeitnehmer_jahresanfang",
)
def ges_krankenv_beitr_satz_zusatzbeitrag_arbeitnehmer_paritätisch_jahresanfang(
    ges_krankenv_zusatzbeitr_satz: float,
    sozialv_beitr_params: dict,
) -> float:
    """Employee's health insurance contribution rate at the beginning of the year.

    Zusatzbeitrag is now split equally between employers and employees.

    Parameters
    ----------
    sozialv_beitr_params
        See params documentation :ref:`sozialv_beitr_params <sozialv_beitr_params>`.

    Returns
    -------

    """
    allgemeiner_beitr_satz = sozialv_beitr_params["beitr_satz_jahresanfang"][
        "ges_krankenv"
    ]["allgemein"]
    return (allgemeiner_beitr_satz + ges_krankenv_zusatzbeitr_satz) / 2


@policy_info(
    end_date="2008-12-31",
    name_in_dag="_ges_krankenv_beitr_satz_arbeitgeber",
)
def ges_krankenv_beitr_satz_arbeitgeber_mean_kassenspezifisch_zusatzbeitrag_nur_arbeitnehmer(  # noqa: E501
    sozialv_beitr_params: dict,
) -> float:
    """Employer's health insurance contribution rate.

    Until 2008, the top-up contribution rate (Zusatzbeitrag) was not considered.

    Parameters
    ----------
    sozialv_beitr_params
        See params documentation :ref:`sozialv_beitr_params <sozialv_beitr_params>`.

    Returns
    -------

    """

    return sozialv_beitr_params["beitr_satz"]["ges_krankenv"]["mean_allgemein"] / 2


@policy_info(
    end_date="2008-12-31",
    name_in_dag="_ges_krankenv_beitr_satz_arbeitgeber_jahresanfang",
)
def ges_krankenv_beitr_satz_arbeitgeber_mean_kassenspezifisch_zusatzbeitrag_nur_arbeitnehmer_jahresanfang(  # noqa: E501
    sozialv_beitr_params: dict,
) -> float:
    """Employer's health insurance contribution rate at the begging of the year.

    Until 2008, the top-up contribution rate (Zusatzbeitrag) was not considered.

    Parameters
    ----------
    sozialv_beitr_params
        See params documentation :ref:`sozialv_beitr_params <sozialv_beitr_params>`.

    Returns
    -------

    """

    return (
        sozialv_beitr_params["beitr_satz_jahresanfang"]["ges_krankenv"][
            "mean_allgemein"
        ]
        / 2
    )


@policy_info(
    start_date="2009-01-01",
    end_date="2018-12-31",
    name_in_dag="_ges_krankenv_beitr_satz_arbeitgeber",
)
def ges_krankenv_beitr_satz_arbeitgeber_einheitlich_zusatzbeitrag_nur_arbeitnehmer(
    sozialv_beitr_params: dict,
) -> float:
    """Employer's health insurance contribution rate.

    From 2009 until 2018, the contribution rate was uniform for all health insurers,
    Zusatzbeitrag irrelevant.

    Parameters
    ----------
    sozialv_beitr_params
        See params documentation :ref:`sozialv_beitr_params <sozialv_beitr_params>`.

    Returns
    -------

    """

    return sozialv_beitr_params["beitr_satz"]["ges_krankenv"]["allgemein"] / 2


@policy_info(
    start_date="2009-01-01",
    end_date="2018-12-31",
    name_in_dag="_ges_krankenv_beitr_satz_arbeitgeber_jahresanfang",
)
def ges_krankenv_beitr_satz_arbeitgeber_einheitlich_zusatzbeitrag_nur_arbeitnehmer_jahresanfang(  # noqa: E501
    sozialv_beitr_params: dict,
) -> float:
    """Employer's health insurance contribution rate at the beginning of the year.

    From 2009 until 2018, the contribution rate was uniform for all health insurers,
    Zusatzbeitrag irrelevant.

    Parameters
    ----------
    sozialv_beitr_params
        See params documentation :ref:`sozialv_beitr_params <sozialv_beitr_params>`.

    Returns
    -------

    """

    return (
        sozialv_beitr_params["beitr_satz_jahresanfang"]["ges_krankenv"]["allgemein"] / 2
    )


@policy_info(
    start_date="2019-01-01",
    name_in_dag="_ges_krankenv_beitr_satz_arbeitgeber",
)
def _ges_krankenv_beitr_satz_arbeitgeber_zusatzbeitrag_paritätisch(
    ges_krankenv_beitr_satz_arbeitnehmer: float,
) -> float:
    """Employer's health insurance contribution rate.

    Since 2019, the full contribution rate is now split equally between employers and
    employees.

    Parameters
    ----------
    ges_krankenv_beitr_satz_arbeitnehmer
        See :func:`ges_krankenv_beitr_satz_arbeitnehmer`.

    Returns
    -------

    """
    return ges_krankenv_beitr_satz_arbeitnehmer


@policy_info(
    start_date="2019-01-01",
    name_in_dag="_ges_krankenv_beitr_satz_arbeitgeber_jahresanfang",
)
def _ges_krankenv_beitr_satz_arbeitgeber_zusatzbeitrag_paritätisch_jahresanfang(
    _ges_krankenv_beitr_satz_arbeitnehmer_jahresanfang: float,
) -> float:
    """Employer's health insurance contribution rate at the beginning of the year.

    Since 2019, the full contribution rate is now split equally between employers and
    employees.

    Parameters
    ----------
    ges_krankenv_beitr_satz_arbeitnehmer
        See :func:`ges_krankenv_beitr_satz_arbeitnehmer`.

    Returns
    -------

    """
    return _ges_krankenv_beitr_satz_arbeitnehmer_jahresanfang


@policy_info(
    start_date="2005-07-01",
    end_date="2014-12-31",
    name_in_dag="ges_krankenv_zusatzbeitr_satz",
)
def ges_krankenv_zusatzbeitr_satz_from_sonderbeitr_satz(
    sozialv_beitr_params: dict,
) -> float:
    """Health insurance top-up (Zusatzbeitrag) rate until December 2014.

    Parameters
    ----------
    sozialv_beitr_params
        See params documentation :ref:`sozialv_beitr_params <sozialv_beitr_params>`.

    Returns
    -------
    Zusatzbeitragssatz (based on Sonderbeitrag)

    """

    return sozialv_beitr_params["beitr_satz"]["ges_krankenv"]["sonderbeitrag"]


@policy_info(
    start_date="2015-01-01",
    name_in_dag="ges_krankenv_zusatzbeitr_satz",
)
def ges_krankenv_zusatzbeitr_satz_from_mean_zusatzbeitrag(
    sozialv_beitr_params: dict,
) -> float:
    """Health insurance top-up rate (Zusatzbeitrag) since January 2015.

    Parameters
    ----------
    sozialv_beitr_params
        See params documentation :ref:`sozialv_beitr_params <sozialv_beitr_params>`.

    Returns
    -------
    Zusatzbeitragssatz (based on mean value of Zusatzbeitragssatz)

    """

    return sozialv_beitr_params["beitr_satz"]["ges_krankenv"]["mean_zusatzbeitrag"]
