//! Unit Quaternions for 3D Spatial Rotations.

#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Quaternion {
    pub w: f64,
    pub x: f64,
    pub y: f64,
    pub z: f64,
}

impl Quaternion {
    pub fn new(w: f64, x: f64, y: f64, z: f64) -> Self {
        Quaternion { w, x, y, z }
    }

    pub fn from_axis_angle(axis: [f64; 3], angle_rad: f64) -> Self {
        let half = 0.5 * angle_rad;
        let s = half.sin();
        let norm = (axis[0] * axis[0] + axis[1] * axis[1] + axis[2] * axis[2]).sqrt();
        Quaternion {
            w: half.cos(),
            x: axis[0] / norm * s,
            y: axis[1] / norm * s,
            z: axis[2] / norm * s,
        }
    }

    pub fn mul(self, q: Self) -> Self {
        Quaternion {
            w: self.w * q.w - self.x * q.x - self.y * q.y - self.z * q.z,
            x: self.w * q.x + self.x * q.w + self.y * q.z - self.z * q.y,
            y: self.w * q.y - self.x * q.z + self.y * q.w + self.z * q.x,
            z: self.w * q.z + self.x * q.y - self.y * q.x + self.z * q.w,
        }
    }

    pub fn conjugate(self) -> Self {
        Quaternion { w: self.w, x: -self.x, y: -self.y, z: -self.z }
    }

    pub fn rotate_vector(self, v: [f64; 3]) -> [f64; 3] {
        let p = Quaternion::new(0.0, v[0], v[1], v[2]);
        let rotated = self.mul(p).mul(self.conjugate());
        [rotated.x, rotated.y, rotated.z]
    }
}
