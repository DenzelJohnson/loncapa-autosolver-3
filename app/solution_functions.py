import math

ke = 8.9875517923e9  # Coulomb constant (N·m^2/C^2)
sqrt = math.sqrt

questions_1D03 = [
  {
    "problem_id": "sf-prob0210a.problem",
    "question_text": "A tortoise can run with a speed of ... How long does the race take?",
    "inputs": ["v_tortoise_cmps", "hare_ratio", "rest_s", "win_margin_cm"],
    "function": "prob_sf_0210a_part1",
    "answer_units": "s",
    "pattern_matcher": "prob0210a",
    "part": 1,
    "prompt": "How long does the race take?",
  },
  {
    "problem_id": "sf-prob0210a.problem",
    "question_text": "What is the length of the race?",
    "inputs": ["v_tortoise_cmps", "hare_ratio", "rest_s", "win_margin_cm"],
    "function": "prob_sf_0210a_part2",
    "answer_units": "m",
    "pattern_matcher": "prob0210a",
    "part": 2,
    "prompt": "What is the length of the race?",
  },
  {
    "problem_id": "sf-prob0218.problem",
    "question_text": "Average acceleration during wall contact",
    "inputs": ["v_in_ms", "v_out_ms", "dt_s"],
    "function": "prob_sf_0218",
    "answer_units": "m/s^2",
    "pattern_matcher": "prob0218",
    "part": 1,
    "prompt": "Average acceleration while in contact",
  },  # Knight 0250a — braking problem
  {
    "problem_id": "kn-prob0250a.problem",
    "question_text": "Distance when brakes applied",
    "inputs": ["v0_ms", "d_m", "t_reaction_s"],
    "function": "prob_kn_0250a_part1",
    "answer_units": "m",
    "pattern_matcher": "kn0250a",
    "part": 1,
    "prompt": "How far are you from the intersection when you begin to apply the brakes?",
  },
  {
    "problem_id": "kn-prob0250a.problem",
    "question_text": "Required acceleration to stop at the intersection",
    "inputs": ["v0_ms", "d_m", "t_reaction_s"],
    "function": "prob_kn_0250a_part2",
    "answer_units": "m/s^2",
    "pattern_matcher": "kn0250a",
    "part": 2,
    "prompt": "What acceleration will bring you to rest as you just reach the intersection?",
  },
  {
    "problem_id": "kn-prob0250a.problem",
    "question_text": "Stopping time after brakes applied",
    "inputs": ["v0_ms", "d_m", "t_reaction_s"],
    "function": "prob_kn_0250a_part3",
    "answer_units": "s",
    "pattern_matcher": "kn0250a",
    "part": 3,
    "prompt": "How long does it take you to stop?",
  },
  # Knight 0258 — constant acceleration
  {
    "problem_id": "kn-prob0258.problem",
    "question_text": "Initial velocity from segment with constant acceleration",
    "inputs": ["a_ms2", "dx_m", "t1_s", "t2_s"],
    "function": "prob_kn_0258",
    "answer_units": "m/s",
    "pattern_matcher": "kn0258",
    "part": 1,
    "prompt": "What was the car's velocity at t=0?",
  },
  # Knight 0266a — circular motion
  {
    "problem_id": "kn-prob0266a.problem",
    "question_text": "Bridge rocks time gap",
    "inputs": ["h_m", "v0_ms"],
    "function": "prob_kn_0266a_part1",
    "answer_units": "s",
    "pattern_matcher": "kn0266a_bridge",
    "part": 1,
    "prompt": "Time between splashes",
  },
  {
    "problem_id": "kn-prob0266a.problem",
    "question_text": "Bridge rocks impact speed",
    "inputs": ["h_m", "v0_ms"],
    "function": "prob_kn_0266a_part2",
    "answer_units": "m/s",
    "pattern_matcher": "kn0266a_bridge",
    "part": 2,
    "prompt": "Impact speed",
  },
  {
    "problem_id": "sb-prob0342.problem",
    "question_text": "Equal vectors sum to j-component",
    "inputs": ["m", "sumj"],
    "function": "prob_sb_0342",
    "answer_units": "deg",
    "pattern_matcher": "sb0342",
    "part": 1,
    "prompt": "Angle between A and B",
  },
  {
    "problem_id": "sb-prob0353.problem",
    "question_text": "Equal vectors ratio condition",
    "inputs": ["k_ratio"],
    "function": "prob_sb_0353",
    "answer_units": "deg",
    "pattern_matcher": "sb0353",
    "part": 1,
    "prompt": "Angle between A and B",
  },
  {
    "problem_id": "sb-prob0416a.problem",
    "question_text": "Projectile from window: range",
    "inputs": ["v0_ms", "theta_deg", "t_s"],
    "function": "prob_sb_0416a_part1",
    "answer_units": "m",
    "pattern_matcher": "sb0416a",
    "part": 1,
    "prompt": "Horizontal distance",
  },
  {
    "problem_id": "sb-prob0416a.problem",
    "question_text": "Projectile from window: height",
    "inputs": ["v0_ms", "theta_deg", "t_s"],
    "function": "prob_sb_0416a_part2",
    "answer_units": "m",
    "pattern_matcher": "sb0416a",
    "part": 2,
    "prompt": "Height of window",
  },
  {
    "problem_id": "sb-prob0416a.problem",
    "question_text": "Projectile from window: time to 11.5 m below",
    "inputs": ["v0_ms", "theta_deg", "t_s"],
    "function": "prob_sb_0416a_part3",
    "answer_units": "s",
    "pattern_matcher": "sb0416a",
    "part": 3,
    "prompt": "Time to y drop",
  },
  {
    "problem_id": "sb-prob0344.problem",
    "question_text": "Buried treasure resultant distance",
    "inputs": ["d1", "ang1_deg", "d2", "ang2_deg", "d3", "ang3_deg"],
    "function": "prob_sb_0344_part1",
    "answer_units": "",
    "pattern_matcher": "sb0344",
    "part": 1,
    "prompt": "Resultant distance",
  },
  {
    "problem_id": "sb-prob0344.problem",
    "question_text": "Buried treasure resultant angle",
    "inputs": ["d1", "ang1_deg", "d2", "ang2_deg", "d3", "ang3_deg"],
    "function": "prob_sb_0344_part2",
    "answer_units": "deg",
    "pattern_matcher": "sb0344",
    "part": 2,
    "prompt": "Resultant angle (from +x)",
  },
  {
    "problem_id": "sf-prob0206a.problem",
    "question_text": "Average velocity from fixed x(t) graph over [t1,t2]",
    "inputs": [],
    "function": "prob_sf_0206a_part1",
    "answer_units": "m/s",
    "pattern_matcher": "prob0206a",
    "part": 1,
    "prompt": "Average velocity",
  },
  {
    "problem_id": "sf-prob0206a.problem",
    "question_text": "Average velocity from fixed x(t) graph over [t1,t2] (part 2)",
    "inputs": [],
    "function": "prob_sf_0206a_part2",
    "answer_units": "m/s",
    "pattern_matcher": "prob0206a",
    "part": 2,
    "prompt": "Average velocity",
  },
  {
    "problem_id": "sf-prob0206a.problem",
    "question_text": "Average velocity from fixed x(t) graph over [t1,t2] (part 3)",
    "inputs": [],
    "function": "prob_sf_0206a_part3",
    "answer_units": "m/s",
    "pattern_matcher": "prob0206a",
    "part": 3,
    "prompt": "Average velocity",
  },
  {
    "problem_id": "sb-prob0441a.problem",
    "question_text": "River rescue: heading relative to shore",
    "inputs": ["v_current_kmh", "d_cross_km", "d_up_km", "v_boat_kmh"],
    "function": "prob_sb_0441a_part1",
    "answer_units": "deg",
    "pattern_matcher": "sb0441a",
    "part": 1,
    "prompt": "Heading relative to shore",
  },
  {
    "problem_id": "sb-prob0441a.problem",
    "question_text": "River rescue: boat ground-velocity angle",
    "inputs": ["v_current_kmh", "d_cross_km", "d_up_km", "v_boat_kmh"],
    "function": "prob_sb_0441a_part2",
    "answer_units": "deg",
    "pattern_matcher": "sb0441a",
    "part": 2,
    "prompt": "Boat velocity angle to shore",
  },
  {
    "problem_id": "sb-prob0441a.problem",
    "question_text": "River rescue: time to intercept",
    "inputs": ["v_current_kmh", "d_cross_km", "d_up_km", "v_boat_kmh"],
    "function": "prob_sb_0441a_part3",
    "answer_units": "h",
    "pattern_matcher": "sb0441a",
    "part": 3,
    "prompt": "Time to intercept",
  },
  {
    "problem_id": "sb-prob0464.problem",
    "question_text": "River speed from log timing",
    "inputs": ["x0_km", "t_up_min"],
    "function": "prob_sb_0464",
    "answer_units": "km/h",
    "pattern_matcher": "sb0464",
    "part": 1,
    "prompt": "River speed",
  },
  {
    "problem_id": "sb-prob0446.problem",
    "question_text": "Radial acceleration from break and landing",
    "inputs": ["r_m", "h_m", "R_m"],
    "function": "prob_sb_0446",
    "answer_units": "m/s^2",
    "pattern_matcher": "sb0446",
    "part": 1,
    "prompt": "Radial acceleration",
  },
  {
    "problem_id": "hr-prob0483.problem",
    "question_text": "Wind speed from ground track",
    "inputs": ["v_air_kmh", "distance_km", "heading_deg", "time_hr"],
    "function": "prob_hr_0483",
    "answer_units": "km/h",
    "pattern_matcher": "hr0483",
    "part": 1,
    "prompt": "Wind speed magnitude",
  },
  {
    "problem_id": "sf-prob0246.problem",
    "question_text": "Two balls same height time",
    "inputs": ["v0_ms", "h_m"],
    "function": "prob_sf_0246",
    "answer_units": "s",
    "pattern_matcher": "prob0246",
    "part": 1,
    "prompt": "After how long are they at the same height?",
  },
  {
    "problem_id": "sf-prob0258.problem",
    "question_text": "Downward throw time to ground",
    "inputs": ["v0_ms", "h_m"],
    "function": "prob_sf_0258",
    "answer_units": "s",
    "pattern_matcher": "prob0258",
    "part": 1,
    "prompt": "Time to hit ground",
  },
  # Knight 0214a (graph-based) — extract variables but solvers require graph info
  {
    "problem_id": "kn-prob0214a.problem",
    "question_text": "Position at t given v-t graph (requires graph)",
    "inputs": ["x0_m", "vmax_ms", "t_total_s", "t_query_s"],
    "function": "prob_kn_0214a_part1",
    "answer_units": "m",
    "pattern_matcher": "kn0214a",
    "part": 1,
    "prompt": "Position at t = ... s",
  },
  {
    "problem_id": "kn-prob0214a.problem",
    "question_text": "Velocity at t given v-t graph (requires graph)",
    "inputs": ["x0_m", "vmax_ms", "t_total_s", "t_query_s"],
    "function": "prob_kn_0214a_part2",
    "answer_units": "m/s",
    "pattern_matcher": "kn0214a",
    "part": 2,
    "prompt": "Velocity at t = ... s",
  },
  {
    "problem_id": "kn-prob0214a.problem",
    "question_text": "Acceleration at t given v-t graph (requires graph)",
    "inputs": ["x0_m", "vmax_ms", "t_total_s", "t_query_s"],
    "function": "prob_kn_0214a_part3",
    "answer_units": "m/s^2",
    "pattern_matcher": "kn0214a",
    "part": 3,
    "prompt": "Acceleration at t = ... s",
  },
  # Knight 0224a — skier on incline
  {
    "problem_id": "kn-prob0224a.problem",
    "question_text": "Length of incline",
    "inputs": ["v0_ms", "theta_deg", "vf_ms"],
    "function": "prob_kn_0224a_part1",
    "answer_units": "m",
    "pattern_matcher": "kn0224a",
    "part": 1,
    "prompt": "What is the length of the incline?",
  },
  {
    "problem_id": "kn-prob0224a.problem",
    "question_text": "Time to bottom",
    "inputs": ["v0_ms", "theta_deg", "vf_ms"],
    "function": "prob_kn_0224a_part2",
    "answer_units": "s",
    "pattern_matcher": "kn0224a",
    "part": 2,
    "prompt": "How long does it take to reach the bottom?",
  },
]

questions_1E03 = [
  {
    "problem_id": "sf-prob1508.problem",
    "question_text": "A 6.00E-9C charge is on the x axis at x = -1.58m and a 1.95E-9C charge is on the x axis at x = 1.88m. Find the net force exerted on a 3.32E-9C charge located at the origin.",
    "inputs": ["q1", "x1", "q2", "x2", "q3"],
    "function": "prob_sf_1508",
    "answer_units": "N",
    "pattern_matcher": "prob1508",
  },
  {
    "problem_id": "sf-prob1514.problem",
    "question_text": "A charge of 2.27E-9C is placed at the origin, and a charge of 4.23E-9C is placed at x = 1.50m. Locate the x coordinate of the point between the two charges at which a charge of 2.83E-9C should be placed so that the net electric force on it is zero.",
    "inputs": ["q1", "q2", "x1", "q3"],
    "function": "prob_sf_1514",
    "answer_units": "m",
    "pattern_matcher": "prob1514",
  },
  # multipart: same problem_id, shared matcher/inputs, different solvers/units/parts
  {
    "problem_id": "sf-prob1560a.problem",
    "question_text": "A charged cork ball of mass ... Calculate the charge on the ball.",
    "inputs": ["m", "x_comp", "y_comp", "deg"],
    "function": "prob_sf_1560a_part1",
    "answer_units": "C",
    "pattern_matcher": "prob1560a",
    "part": 1,
    "prompt": "Calculate the charge on the ball",
  },
  {
    "problem_id": "sf-prob1560a.problem",
    "question_text": "Calculate the tension in the string.",
    "inputs": ["m", "x_comp", "y_comp", "deg"],
    "function": "prob_sf_1560a_part2",
    "answer_units": "N",
    "pattern_matcher": "prob1560a",
    "part": 2,
    "prompt": "Calculate the tension in the string",
  },
]

# Aliases with the literal names requested (not valid Python identifiers for direct use)
globals()["1D03_questions"] = questions_1D03
globals()["1E03_questions"] = questions_1E03

# Indexes are built at the end of the file after all question lists are defined.











# Physics 1D03 Solutions Functions


def prob_sf_0210a_part1(v_tortoise_cmps=None, hare_ratio=None, rest_s=None, win_margin_cm=None):
    """Return race duration T (s) where tortoise wins by win_margin_cm.
    Inputs are numeric values as strings/floats with units implied by names.
    v_tortoise_cmps: cm/s, hare_ratio: unitless, rest_s: s, win_margin_cm: cm
    """
    if None in (v_tortoise_cmps, hare_ratio, rest_s, win_margin_cm):
        raise ValueError("tortoise_hare_time requires v_tortoise_cmps, hare_ratio, rest_s, win_margin_cm")
    v = float(v_tortoise_cmps)           # cm/s
    r = float(hare_ratio)
    R = float(rest_s)                    # s
    dwin = float(win_margin_cm)          # cm
    vh = r * v                           # cm/s
    denom = (vh - v)
    if abs(denom) < 1e-12:
        raise ValueError("hare speed must exceed tortoise speed")
    T = (vh * R - dwin) / denom          # s
    if T <= 0:
        raise ValueError("non-physical race time")
    return T


def prob_sf_0210a_part2(v_tortoise_cmps=None, hare_ratio=None, rest_s=None, win_margin_cm=None):
    """Return race length (m). Uses T from prob_sf_0210a_part1 and v in cm/s."""
    T = prob_sf_0210a_part1(v_tortoise_cmps, hare_ratio, rest_s, win_margin_cm)  # s
    v = float(v_tortoise_cmps)  # cm/s
    L_cm = v * T                # cm
    L_m = L_cm / 100.0         # m
    return L_m


def prob_sf_0218(v_in_ms=None, v_out_ms=None, dt_s=None):
    """Average acceleration magnitude during a bounce against a wall.
    v_in_ms: incident speed (m/s), v_out_ms: rebound speed magnitude (m/s), dt_s: contact time (s).
    Assumes velocity reverses direction during contact; returns positive magnitude.
    """
    if None in (v_in_ms, v_out_ms, dt_s):
        raise ValueError("avg_accel_rebound requires v_in_ms, v_out_ms, dt_s")
    vi = float(v_in_ms)
    vo = float(v_out_ms)
    dt = float(dt_s)
    if dt <= 0:
        raise ValueError("dt must be > 0")
    # initial +vi toward wall, final velocity is -vo away from wall
    delta_v = (-vo) - (+vi)
    a = abs(delta_v) / dt
    return a


def prob_sf_0246(v0_ms=None, h_m=None):
    """Time when y_ground_ball == y_dropped_ball given same start time.
    Ground ball: y1 = v0*t - 1/2 g t^2; Dropped ball: y2 = h - 1/2 g t^2 -> v0*t = h => t=h/v0
    """
    if None in (v0_ms, h_m):
        raise ValueError("two_balls_meet_time requires v0_ms, h_m")
    v0 = float(v0_ms)
    h = float(h_m)
    if v0 <= 0:
        raise ValueError("v0 must be > 0")
    return h / v0


def prob_kn_0258(a_ms2=None, dx_m=None, t1_s=None, t2_s=None):
    """Given constant acceleration a, displacement between t1 and t2 (dx), compute v0.
    dx = v0*(t2-t1) + 0.5*a*(t2^2 - t1^2) -> v0 = (dx - 0.5*a*(t2^2 - t1^2)) / (t2 - t1)
    """
    if None in (a_ms2, dx_m, t1_s, t2_s):
        raise ValueError("initial_velocity_from_segment requires a_ms2, dx_m, t1_s, t2_s")
    a = float(a_ms2)
    dx = float(dx_m)
    t1 = float(t1_s)
    t2 = float(t2_s)
    if t2 == t1:
        raise ValueError("t2 must differ from t1")
    v0 = (dx - 0.5 * a * (t2*t2 - t1*t1)) / (t2 - t1)
    return v0


def prob_kn_0214a_part1(x0_m=None, vmax_ms=None, t_total_s=None, t_query_s=None):
    """Position at time t given a linear v-t graph: v(t) = (vmax/t_total) * t for 0<=t<=t_total.
    Uses x(t) = x0 + ∫ v dt = x0 + 0.5*(vmax/t_total)*t^2. Times beyond t_total are clamped to t_total.
    """
    if None in (x0_m, vmax_ms, t_total_s, t_query_s):
        raise ValueError("kn0214_position requires x0_m, vmax_ms, t_total_s, t_query_s")
    x0 = float(x0_m)
    vmax = float(vmax_ms)
    T = float(t_total_s)
    t = min(max(float(t_query_s), 0.0), T) if T > 0 else float(t_query_s)
    if T <= 0:
        raise ValueError("t_total must be positive")
    a = vmax / T
    x = x0 + 0.5 * a * t * t
    return x


def prob_kn_0214a_part2(x0_m=None, vmax_ms=None, t_total_s=None, t_query_s=None):
    """Velocity at time t for linear ramp: v(t) = (vmax/t_total) * t, clamped to [0, vmax]."""
    if None in (vmax_ms, t_total_s, t_query_s):
        raise ValueError("kn0214_velocity requires vmax_ms, t_total_s, t_query_s")
    vmax = float(vmax_ms)
    T = float(t_total_s)
    if T <= 0:
        raise ValueError("t_total must be positive")
    t = float(t_query_s)
    v = (vmax / T) * t
    # Clamp to [0, vmax]
    if v < 0:
        v = 0.0
    if v > vmax:
        v = vmax
    return v


def prob_kn_0214a_part3(x0_m=None, vmax_ms=None, t_total_s=None, t_query_s=None):
    """Constant acceleration (slope) for the linear ramp: a = vmax/t_total."""
    if None in (vmax_ms, t_total_s):
        raise ValueError("kn0214_acceleration requires vmax_ms, t_total_s")
    vmax = float(vmax_ms)
    T = float(t_total_s)
    if T <= 0:
        raise ValueError("t_total must be positive")
    return vmax / T


def prob_kn_0224a_part1(v0_ms=None, theta_deg=None, vf_ms=None):
    if None in (v0_ms, theta_deg, vf_ms):
        raise ValueError("incline_length requires v0_ms, theta_deg, vf_ms")
    v0 = float(v0_ms)
    vf = float(vf_ms)
    theta = math.radians(float(theta_deg))
    g = 9.80665
    a = g * math.sin(theta)
    if a <= 0:
        raise ValueError("invalid angle for downhill acceleration")
    s = (vf*vf - v0*v0) / (2.0 * a)
    return s


def prob_kn_0224a_part2(v0_ms=None, theta_deg=None, vf_ms=None):
    if None in (v0_ms, theta_deg, vf_ms):
        raise ValueError("incline_time requires v0_ms, theta_deg, vf_ms")
    v0 = float(v0_ms)
    vf = float(vf_ms)
    theta = math.radians(float(theta_deg))
    g = 9.80665
    a = g * math.sin(theta)
    if a <= 0:
        raise ValueError("invalid angle for downhill acceleration")
    t = (vf - v0) / a
    return t


def prob_sb_0416a_part1(v0_ms=None, theta_deg=None, t_s=None):
    if None in (v0_ms, theta_deg, t_s):
        raise ValueError("proj_window_range requires v0_ms, theta_deg, t_s")
    v0 = float(v0_ms)
    theta = math.radians(float(theta_deg))
    t = float(t_s)
    return v0 * math.cos(-theta) * t


def prob_sb_0416a_part2(v0_ms=None, theta_deg=None, t_s=None):
    if None in (v0_ms, theta_deg, t_s):
        raise ValueError("proj_window_height requires v0_ms, theta_deg, t_s")
    v0 = float(v0_ms)
    theta = math.radians(float(theta_deg))
    t = float(t_s)
    g = 9.80665
    # y = h - v0*sin(theta)*t - 0.5 g t^2; solve for h
    h = v0 * math.sin(theta) * t + 0.5 * g * t * t
    return h


def prob_sb_0416a_part3(v0_ms=None, theta_deg=None, t_s=None):
    """Time to be 11.5 m below the launch height for a launch angle below horizontal.
    Uses fixed drop of 11.5 m to align with resource wording.
    """
    if None in (v0_ms, theta_deg):
        raise ValueError("proj_time_to_drop requires v0_ms, theta_deg")
    v0 = float(v0_ms)
    theta = math.radians(float(theta_deg))
    yd = 11.5
    g = 9.80665
    # Equation: -v0*sin(theta)*t - 0.5 g t^2 = -yd ⇒ 0.5 g t^2 + v0*sin(theta) t - yd = 0
    a = 0.5 * g
    b = v0 * math.sin(theta)
    c = -yd
    disc = b*b - 4*a*c
    t1 = (-b + math.sqrt(disc)) / (2*a)
    t2 = (-b - math.sqrt(disc)) / (2*a)
    return max(t1, t2)


def prob_sb_0344_part1(d1=None, ang1_deg=None, d2=None, ang2_deg=None, d3=None, ang3_deg=None):
    if None in (d1, ang1_deg, d2, ang2_deg, d3, ang3_deg):
        raise ValueError("treasure_resultant_distance requires all legs")
    import math as _m
    def comp(d, ang):
        a = _m.radians(float(ang))
        return float(d)*_m.cos(a), float(d)*_m.sin(a)
    x1,y1 = comp(d1, ang1_deg)
    x2,y2 = comp(d2, ang2_deg)
    x3,y3 = comp(d3, ang3_deg)
    X = x1+x2+x3
    Y = y1+y2+y3
    return math.hypot(X, Y)


def prob_sb_0344_part2(d1=None, ang1_deg=None, d2=None, ang2_deg=None, d3=None, ang3_deg=None):
    if None in (d1, ang1_deg, d2, ang2_deg, d3, ang3_deg):
        raise ValueError("treasure_resultant_angle requires all legs")
    import math as _m
    def comp(d, ang):
        a = _m.radians(float(ang))
        return float(d)*_m.cos(a), float(d)*_m.sin(a)
    x1,y1 = comp(d1, ang1_deg)
    x2,y2 = comp(d2, ang2_deg)
    x3,y3 = comp(d3, ang3_deg)
    X = x1+x2+x3
    Y = y1+y2+y3
    ang = math.degrees(math.atan2(Y, X))
    if ang < 0:
        ang += 360.0
    return ang


def prob_sf_0206a(t1_s=None, t2_s=None):
    """Average velocity over [t1,t2] for the fixed piecewise x(t) shown in the image.
    Graph interpretation (units: t in s, x in m):
      Segment A: 0 ≤ t ≤ 1.0      x(t) = 4 t
      Segment B: 1.0 < t ≤ 2.5    x(t) = 8 − 4 t
      Segment C: 2.5 < t ≤ 3.5    x(t) = −2
      Segment D: 3.5 < t ≤ 5.0    x(t) = −2 + (4/3)(t − 3.5)
    """
    if None in (t1_s, t2_s):
        raise ValueError("avg_velocity_from_fixed_xt requires t1_s, t2_s")
    t1 = float(t1_s)
    t2 = float(t2_s)
    if t2 == t1:
        return 0.0

    def x_of(t: float) -> float:
        if t <= 0.0:
            return 0.0
        if t <= 1.0:
            return 4.0 * t
        if t <= 2.5:
            return 8.0 - 4.0 * t
        if t <= 3.5:
            return -2.0
        if t <= 5.0:
            return -2.0 + (4.0/3.0) * (t - 3.5)
        # Extrapolate last segment if needed
        return -2.0 + (4.0/3.0) * (t - 3.5)

    return (x_of(t2) - x_of(t1)) / (t2 - t1)

def prob_sf_0206a_part1():
    return prob_sf_0206a(0.0, 1.0)

def prob_sf_0206a_part2():
    return prob_sf_0206a(0.0, 2.0)

def prob_sf_0206a_part3():
    return prob_sf_0206a(1.0, 5.0)


# Build indexes now that all question lists are defined
CATALOG_BY_ID = {q["problem_id"]: q for q in (questions_1E03 + questions_1D03)}
CATALOG_GROUPED_BY_ID = {}
for q in (questions_1E03 + questions_1D03):
    CATALOG_GROUPED_BY_ID.setdefault(q["problem_id"], []).append(q)


def prob_sb_0441a_part1(v_current_kmh=None, d_cross_km=None, d_up_km=None, v_boat_kmh=None):
    if None in (v_current_kmh, d_cross_km, d_up_km, v_boat_kmh):
        raise ValueError("river_rescue_heading requires v_current_kmh, d_cross_km, d_up_km, v_boat_kmh")
    # Heading relative to shore to intercept: theta = atan2(y0, x0), independent of current
    y0 = float(d_cross_km)
    x0 = float(d_up_km)
    alpha_deg = math.degrees(math.atan2(y0, x0))
    return alpha_deg


def prob_sb_0441a_part2(v_current_kmh=None, d_cross_km=None, d_up_km=None, v_boat_kmh=None):
    if None in (d_cross_km, d_up_km):
        raise ValueError("river_rescue_boat_angle requires d_cross_km, d_up_km")
    y0 = float(d_cross_km)
    x0 = float(d_up_km)
    # Ground-track direction to the target is the geometric angle to the point
    phi_deg = math.degrees(math.atan2(y0, x0))
    return phi_deg


def prob_sb_0441a_part3(v_current_kmh=None, d_cross_km=None, d_up_km=None, v_boat_kmh=None):
    if None in (v_current_kmh, d_cross_km, d_up_km, v_boat_kmh):
        raise ValueError("river_rescue_time requires v_current_kmh, d_cross_km, d_up_km, v_boat_kmh")
    vb = float(v_boat_kmh)
    y0 = float(d_cross_km)
    x0 = float(d_up_km)
    theta = math.atan2(y0, x0)
    # Time to intercept: t = y0 / (vb * sin(theta)) = x0 / (vb * cos(theta)) (hours)
    s = vb * math.sin(theta)
    if abs(s) < 1e-12:
        raise ValueError("boat cross-speed too small")
    t_h = y0 / s
    return t_h


def prob_sb_0464(x0_km=None, t_up_min=None):
    if None in (x0_km, t_up_min):
        raise ValueError("river_velocity_from_log requires x0_km, t_up_min")
    x0 = float(x0_km)
    t_h = float(t_up_min) / 60.0
    if t_h <= 0:
        raise ValueError("time must be positive")
    # Result for this classic setup: river speed u = x0 / (2 * t_up)
    return x0 / (2.0 * t_h)


def prob_sb_0446(r_m=None, h_m=None, R_m=None):
    if None in (r_m, h_m, R_m):
        raise ValueError("radial_accel_from_break requires r_m, h_m, R_m")
    r = float(r_m)
    h = float(h_m)
    R = float(R_m)
    g = 9.80665
    # Time of fall from height h: t = sqrt(2h/g)
    t = math.sqrt(2.0 * h / g)
    # Horizontal speed equals tangential speed at break: vx = R / t
    vx = R / t
    # Radial acceleration a = v^2 / r
    return (vx * vx) / r


def prob_hr_0483(v_air_kmh=None, distance_km=None, heading_deg=None, time_hr=None):
    if None in (v_air_kmh, distance_km, heading_deg, time_hr):
        raise ValueError("wind_speed_from_track requires v_air_kmh, distance_km, heading_deg, time_hr")
    v_air = float(v_air_kmh)
    d = float(distance_km)
    t = float(time_hr)
    heading = math.radians(float(heading_deg))
    # Ground speed magnitude from distance/time
    v_g = d / t
    # Desired ground track is due north. Airspeed vector is at heading east of north.
    # Components: V_air = (v_air * sin(heading), v_air * cos(heading)) in (east,north)
    # Ground: V_g = (0, v_g) = V_air + V_wind => V_wind = (-v_air*sin(heading), v_g - v_air*cos(heading))
    vx_w = -v_air * math.sin(heading)
    vy_w = v_g - v_air * math.cos(heading)
    return math.hypot(vx_w, vy_w)


def prob_sf_0258(v0_ms=None, h_m=None):
    """Time to hit ground when thrown straight down from height h with initial speed v0.
    Solve 0.5 g t^2 + v0 t - h = 0 and return positive root.
    """
    if None in (v0_ms, h_m):
        raise ValueError("time_to_ground_downward requires v0_ms, h_m")
    v0 = float(v0_ms)
    h = float(h_m)
    g = 9.80665
    a = 0.5 * g
    b = v0
    c = -h
    disc = b*b - 4*a*c
    if disc < 0:
        raise ValueError("no real impact time")
    t1 = (-b + math.sqrt(disc)) / (2*a)
    t2 = (-b - math.sqrt(disc)) / (2*a)
    return max(t1, t2)


# Physcis 1E03 Solutions Functions

def prob_sf_1508(q1=None, x1=None, q2=None, x2=None, q3=None):
    """Calculate net force magnitude on q3 at origin due to q1 at x1 and q2 at x2 (1D)."""
    if q1 is None or x1 is None or q2 is None or x2 is None or q3 is None:
        raise ValueError("three_charges requires parameters: q1, x1, q2, x2, q3")
    
    # Coulomb contributions (scalar magnitudes)
    fq1 = (q1*q3)/(abs(x1))**2
    fq2 = (q2*q3)/(abs(x2))**2

    # Direction: charges on opposite sides of origin; net at origin is difference in magnitudes
    fnet = ke * (fq1 - fq2)
    return abs(fnet)


def prob_sf_1514(q1=None, q2=None, x1=None, q3=None):
    """Find x between two charges at 0 and x1 where net force on test charge is zero (1D)."""
    if q1 is None or q2 is None or x1 is None or q3 is None:
        raise ValueError("middle requires parameters: q1, q2, x1, q3")

    # Solve for x in (k*q1/x^2) = (k*q2/(x1-x)^2) with x in (0, x1)
    # Taking square roots: sqrt(q1)/|x| = sqrt(q2)/|x1-x|
    # Assume positive distances in segment (0, x1)
    r = math.sqrt(abs(q1)/abs(q2))
    # r = (x)/(x1-x) -> r*(x1-x) = x -> r*x1 = x*(1+r) -> x = r*x1/(1+r)
    x = (r * x1) / (1.0 + r)
    return x


# Shared core for the hanging ball in E-field
# Returns a dict with reusable quantities; expects SI units and degrees for angle

def ball_hanging_core(m=None, x_comp=None, y_comp=None, deg=None):
    if m is None or x_comp is None or y_comp is None or deg is None:
        raise ValueError("ball_hanging_* requires m, x_comp, y_comp, deg")
    theta = math.radians(deg)
    g = 9.80665
    Ex, Ey = x_comp, y_comp

    # Equilibrium equations derivation in pipeline comments
    s, c = math.sin(theta), math.cos(theta)
    if abs(s) < 1e-12:
        raise ValueError("theta too small for stable computation")
    denom = (Ey - (Ex * c / s))
    if abs(denom) < 1e-18:
        raise ValueError("degenerate field/angle configuration")
    q = (m * g) / denom
    T = abs(-q * Ex / s)
    return {"theta": theta, "q": q, "T": T, "Ex": Ex, "Ey": Ey}


def prob_sf_1560a_part1(m=None, x_comp=None, y_comp=None, deg=None):
    return ball_hanging_core(m, x_comp, y_comp, deg)["q"]


def prob_sf_1560a_part2(m=None, x_comp=None, y_comp=None, deg=None):
    return ball_hanging_core(m, x_comp, y_comp, deg)["T"]


def prob_kn_0266a_part1(h_m=None, v0_ms=None):
    if None in (h_m, v0_ms):
        raise ValueError("bridge_time_gap requires h_m, v0_ms")
    g = 9.80665
    h = float(h_m)
    v0 = float(v0_ms)
    # Time for down-thrown rock: solve 0.5 g t^2 + v0 t - h = 0
    a = 0.5 * g
    b = v0
    c = -h
    disc = b*b - 4*a*c
    t_down = (-b + math.sqrt(disc)) / (2*a)
    # Time for up-thrown rock: rise then fall total: t_up = v0/g + sqrt((v0/g)^2 + 2h/g)
    t_up = v0 / g + math.sqrt((v0/g)**2 + 2*h/g)
    return abs(t_up - t_down)


def prob_kn_0266a_part2(h_m=None, v0_ms=None):
    if None in (h_m, v0_ms):
        raise ValueError("bridge_impact_speed requires h_m, v0_ms")
    g = 9.80665
    h = float(h_m)
    v0 = float(v0_ms)
    # Energy: v^2 = v0^2 + 2 g h for both (same magnitude)
    v = math.sqrt(v0*v0 + 2*g*h)
    return v


def prob_sb_0342(m=None, sumj=None):
    if None in (m, sumj):
        raise ValueError("angle_from_equal_vectors_sumj requires m, sumj")
    m = float(m)
    Sy = float(sumj)
    # For equal |A|=|B|=m and A+B = (0, Sy), magnitude of sum is 2 m cos(phi) along y-axis
    # A = m[cos a, sin a], B = m[cos b, sin b]. Maximize simplicity: symmetric about y ⇒ a=90+θ, b=90-θ ⇒ sum_y=2m cos θ
    # Then angle between A and B is 2θ, and 2m cos θ = Sy ⇒ cos θ = Sy/(2m)
    cos_theta = Sy / (2.0 * m)
    if abs(cos_theta) > 1:
        raise ValueError("infeasible inputs: Sy/(2m) out of [-1,1]")
    theta = math.degrees(math.acos(cos_theta))
    return 2.0 * theta


def prob_sb_0353(k_ratio=None):
    if k_ratio is None:
        raise ValueError("angle_from_sum_diff_ratio requires k_ratio")
    k = float(k_ratio)
    # For equal magnitudes m: |A+B| = 2 m cos(Δ/2), |A-B| = 2 m sin(Δ/2)
    # Given |A+B| = k |A-B| ⇒ cot(Δ/2) = k ⇒ Δ/2 = arctan(1/k)
    delta_half = math.degrees(math.atan2(1.0, k))
    return 2.0 * delta_half


# Renamed braking problem functions

def prob_kn_0250a_part1(v0_ms=None, d_m=None, t_reaction_s=None):
    """Distance from intersection when brakes are applied.
    During reaction time, car travels v0 * t_reaction.
    Distance remaining = total_distance - distance_traveled_during_reaction
    """
    if None in (v0_ms, d_m, t_reaction_s):
        raise ValueError("braking_distance_when_applied requires v0_ms, d_m, t_reaction_s")
    v0 = float(v0_ms)
    d_total = float(d_m)
    t_reaction = float(t_reaction_s)
    
    if t_reaction < 0:
        raise ValueError("reaction time must be non-negative")
    
    # Distance traveled during reaction time
    d_reaction = v0 * t_reaction
    
    # Distance remaining when brakes are applied
    d_remaining = d_total - d_reaction
    return d_remaining


def prob_kn_0250a_part2(v0_ms=None, d_m=None, t_reaction_s=None):
    """Constant acceleration needed so that the car stops exactly at the intersection.
    Uses distance remaining after reaction, then v_f^2 = v0^2 + 2 a d => a = -v0^2/(2 d).
    Returns a (negative value for deceleration).
    """
    if None in (v0_ms, d_m, t_reaction_s):
        raise ValueError("required_deceleration_to_stop requires v0_ms, d_m, t_reaction_s")
    v0 = float(v0_ms)
    d_remaining = prob_kn_0250a_part1(v0_ms, d_m, t_reaction_s)
    if d_remaining <= 0:
        raise ValueError("no remaining distance to brake")
    a = - (v0 * v0) / (2.0 * d_remaining)
    return a


def prob_kn_0250a_part3(v0_ms=None, d_m=None, t_reaction_s=None, include_reaction=True):
    """Total time until full stop.
    If include_reaction=True (default): returns reaction time + braking time.
    If include_reaction=False: returns braking time only.
    Uses the constant deceleration from required_deceleration_to_stop().
    """
    if None in (v0_ms, d_m, t_reaction_s):
        raise ValueError("stopping_time_after_brakes requires v0_ms, d_m, t_reaction_s")
    v0 = float(v0_ms)
    a = prob_kn_0250a_part2(v0_ms, d_m, t_reaction_s)
    if a >= 0:
        raise ValueError("acceleration must be negative to stop")
    t_brake = -v0 / a
    return (t_reaction_s + t_brake) if include_reaction else t_brake


