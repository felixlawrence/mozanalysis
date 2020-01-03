# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import attr

from mozanalysis.metrics import agg_any


@attr.s(frozen=True, slots=True)
class Segment(object):
    name = attr.ib(validator=attr.validators.instance_of(str))
    select_expr = attr.ib(validator=attr.validators.instance_of(str))


_segment_list = [
    Segment(
        'country_us',
        agg_any("country = 'US'"),
    ),

    Segment(
        'country_tier_1',
        agg_any("country IN ('US', 'UK', 'DE', 'FR', 'CA')"),
    ),

    Segment(
        'os_windows',
        agg_any("os = 'Windows_NT'"),
    ),

    Segment(
        'os_mac',
        agg_any("os = 'Darwin'"),
    ),

    Segment(
        'os_linux',
        agg_any("os = 'Linux'"),
    ),

    Segment(
        'new_profile',
        agg_any("days_since_created_profile = 0"),
    ),

    Segment(
        'profile_gte_7d',
        agg_any("days_since_created_profile >= 7"),
    ),

    Segment(
        'seen_0_days_in_past_month',
        agg_any("BIT_COUNT(days_seen_bits >> 1) = 0"),
    ),

    Segment(
        'seen_gte1_days_in_past_month',
        agg_any("BIT_COUNT(days_seen_bits >> 1) >= 1"),
    ),

    Segment(
        'seen_gte2_days_in_past_month',
        agg_any("BIT_COUNT(days_seen_bits >> 1) >= 2"),
    ),

    Segment(
        'seen_0_days_in_past_week',
        agg_any("BIT_COUNT(127 & (days_seen_bits >> 1)) = 0"),
    ),

    Segment(
        'seen_gte5_days_in_past_week',
        agg_any("BIT_COUNT(127 & (days_seen_bits >> 1)) >= 5"),
    ),
]


segments = {s.name: s for s in _segment_list}
