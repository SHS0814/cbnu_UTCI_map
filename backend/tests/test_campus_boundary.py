"""The committed campus boundary (data/cbnu_campus_boundary.geojson)."""

import json

from shapely.geometry import Point, shape

from app.config import DATA_DIR, settings
from app.services.geometry import to_projected


def test_boundary_is_a_valid_campus_sized_multipolygon() -> None:
    collection = json.loads((DATA_DIR / "cbnu_campus_boundary.geojson").read_text(encoding="utf-8"))
    (feature,) = collection["features"]
    boundary = shape(feature["geometry"])

    assert boundary.geom_type == "MultiPolygon" and boundary.is_valid
    assert boundary.contains(Point(settings.campus_longitude, settings.campus_latitude))
    assert 80 < to_projected(boundary).area / 10_000 < 100  # hectares; OSM has about 88
