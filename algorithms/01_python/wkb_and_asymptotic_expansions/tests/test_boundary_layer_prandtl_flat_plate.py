from boundary_layer_prandtl_flat_plate import blasius_boundary_thickness


def test_blasius():
    d = blasius_boundary_thickness(1.0, 10000.0)
    assert d == 0.05
