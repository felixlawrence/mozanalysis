# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from mozanalysis.bq_util import sanitize_table_name_for_bq


def test_innocuous_not_changed():
    innocuous_name = 'this_is_an_ok_name'
    assert sanitize_table_name_for_bq(innocuous_name) == innocuous_name


def test_character_censorship():
    bad_name = 'hi-there!-30$'
    assert sanitize_table_name_for_bq(bad_name) == 'hi_there__30_'


def test_really_long_truncated():
    bad_name = 'a' * 2000 + 'rgh'
    shorter = sanitize_table_name_for_bq(bad_name)
    assert len(shorter) == 1003
    assert shorter[:500] == 'a' * 500
    assert shorter[500:503] == '___'
    assert shorter[503:] == 'a' * 497 + 'rgh'
