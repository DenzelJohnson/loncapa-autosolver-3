import re
from typing import List, Dict, Callable

# Matches scientific notation values like 6.00E-9 or -1.5E+3
SCI_NUM_RE = r"[+-]?\d+(?:\.\d+)?E[+-]?\d+"
# Matches plain decimals like -1.58 or 1.50 (without unit)
DEC_NUM_RE = r"[+-]?\d+(?:\.\d+)?"


def prob1508(html_or_text: str) -> List[str]:
    """Extract q1, x1, q2, x2, q3 from the problem statement for sf-prob1508.
    Returns strings preserving scientific notation/formatting.
    """
    charges = re.findall(fr"({SCI_NUM_RE})\s*C", html_or_text, flags=re.IGNORECASE)
    positions = re.findall(fr"x\s*=\s*({DEC_NUM_RE})\s*m", html_or_text, flags=re.IGNORECASE)
    if len(charges) < 3 or len(positions) < 2:
        raise ValueError("Could not extract all variables for prob1508")
    q1, q2, q3 = charges[0], charges[1], charges[2]
    x1, x2 = positions[0], positions[1]
    return [q1, x1, q2, x2, q3]


def prob1514(html_or_text: str) -> List[str]:
    """Extract q1, q2, x1, q3 from the problem statement for sf-prob1514.
    Returns strings preserving scientific notation/formatting.
    """
    charges = re.findall(fr"({SCI_NUM_RE})\s*C", html_or_text, flags=re.IGNORECASE)
    x_match = re.search(fr"x\s*=\s*({DEC_NUM_RE})\s*m", html_or_text, flags=re.IGNORECASE)
    if len(charges) < 3 or not x_match:
        raise ValueError("Could not extract all variables for prob1514")
    q1, q2, q3 = charges[0], charges[1], charges[2]
    x1 = x_match.group(1)
    return [q1, q2, x1, q3]


def prob1560a(html_or_text: str) -> List[str]:
    """Extract m (kg), x_comp (N/C), y_comp (N/C), deg from the statement for sf-prob1560a."""
    text = html_or_text
    # mass like 1.32g or 0.00132 kg
    m_match = re.search(r"mass\s*([0-9]+(?:\.[0-9]+)?)\s*(g|kg)", text, flags=re.IGNORECASE)
    if not m_match:
        raise ValueError("mass not found")
    m_val = float(m_match.group(1))
    m_unit = m_match.group(2).lower()
    m_kg = m_val / 1000.0 if m_unit == "g" else m_val

    x_match = re.search(fr"x\s*component\s*of\s*({SCI_NUM_RE}|{DEC_NUM_RE})\s*N\s*/\s*C", text, flags=re.IGNORECASE)
    y_match = re.search(fr"y\s*component\s*of\s*({SCI_NUM_RE}|{DEC_NUM_RE})\s*N\s*/\s*C", text, flags=re.IGNORECASE)
    if not x_match or not y_match:
        raise ValueError("field components not found")
    x_comp = x_match.group(1)
    y_comp = y_match.group(1)

    # angle: θ = 35.2° or theta = 35.2 deg
    theta_match = re.search(r"(θ|theta)\s*=\s*([0-9]+(?:\.[0-9]+)?)", text, flags=re.IGNORECASE)
    if not theta_match:
        raise ValueError("angle not found")
    deg = theta_match.group(2)

    return [f"{m_kg}", x_comp, y_comp, deg]


def prob0210a(html_or_text: str) -> List[str]:
    """Extract v_tortoise_cmps, hare_ratio, rest_s, win_margin_cm from the tortoise/hare statement.
    Keeps numbers as strings; units assumed as written in prompt.
    """
    text = html_or_text
    # v_tortoise in cm/s e.g., 11.9cm/s
    v_match = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*cm\s*/\s*s", text, flags=re.IGNORECASE)
    # hare_ratio e.g., 19.4 times
    r_match = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*times\s+as\s+fast", text, flags=re.IGNORECASE)
    # rest time in seconds e.g., 124 seconds
    rest_match = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*seconds", text, flags=re.IGNORECASE)
    # win margin e.g., 19.0cm
    margin_match = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*cm\b", text, flags=re.IGNORECASE)

    if not (v_match and r_match and rest_match and margin_match):
        raise ValueError("Could not extract all variables for prob0210a")

    v = v_match.group(1)
    ratio = r_match.group(1)
    rest = rest_match.group(1)
    margin = margin_match.group(1)
    return [v, ratio, rest, margin]


def prob0218(html_or_text: str) -> List[str]:
    """Extract v_in_ms, v_out_ms, dt_s for average-acceleration-on-wall-contact problem."""
    text = html_or_text
    vin = re.search(r"velocity\s+of\s+([0-9]+(?:\.[0-9]+)?)\s*m\s*/\s*s", text, flags=re.IGNORECASE)
    vout = re.search(r"speed\s+of\s+([0-9]+(?:\.[0-9]+)?)\s*m\s*/\s*s", text, flags=re.IGNORECASE)
    dt = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*s\b|([0-9]+(?:\.[0-9]+)?)\s*seconds", text, flags=re.IGNORECASE)
    if not vin or not vout or not dt:
        raise ValueError("Could not extract variables for prob0218")
    v_in = vin.group(1)
    v_out = vout.group(1)
    dt_s = dt.group(1) or dt.group(2)
    return [v_in, v_out, dt_s]


def prob0246(html_or_text: str) -> List[str]:
    """Extract v0_ms (upward) and h_m from the two-balls problem."""
    text = html_or_text
    v0 = re.search(r"initial\s+speed\s+of\s+([0-9]+(?:\.[0-9]+)?)\s*m\s*/\s*s", text, flags=re.IGNORECASE)
    h = re.search(r"building\s+([0-9]+(?:\.[0-9]+)?)\s*m\b|height\s+of\s+([0-9]+(?:\.[0-9]+)?)\s*m\b", text, flags=re.IGNORECASE)
    if not v0 or not h:
        raise ValueError("Could not extract variables for prob0246")
    v0_ms = v0.group(1)
    h_m = h.group(1) or h.group(2)
    return [v0_ms, h_m]


def prob0258(html_or_text: str) -> List[str]:
    """Extract v0_ms and h_m for Serway 0258 (downward throw, time to ground)."""
    text = html_or_text
    v0 = re.search(r"initial\s*(?:speed|velocity)\s*of\s*([0-9]+(?:\.[0-9]+)?)\s*m\s*/\s*s", text, flags=re.IGNORECASE)
    h = re.search(r"height\s*of\s*([0-9]+(?:\.[0-9]+)?)\s*m\b", text, flags=re.IGNORECASE)
    if not v0 or not h:
        # Fallbacks: take first m/s and first standalone meters value
        if not v0:
            v0 = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*m\s*/\s*s", text, flags=re.IGNORECASE)
        if not h:
            m_list = re.findall(r"([0-9]+(?:\.[0-9]+)?)\s*m\b(?!\s*/\s*s)", text, flags=re.IGNORECASE)
            if m_list:
                class _MH:
                    def __init__(self, v): self._v = v
                    def group(self, i): return self._v
                h = _MH(m_list[0])
    if not v0 or not h:
        raise ValueError("Could not extract variables for prob0258")
    return [v0.group(1), h.group(1)]


def prob0206a(html_or_text: str) -> List[str]:
    """Extract one or more intervals [t1, t2] from the statement.
    Returns either [t1, t2] (single interval) or [[t1a, t2a], [t1b, t2b], ...] for multipart.
    """
    text = html_or_text
    pairs = re.findall(r"time\s+interval\s*([0-9]+(?:\.[0-9]+)?)\s*s\s*to\s*([0-9]+(?:\.[0-9]+)?)\s*s", text, flags=re.IGNORECASE)
    if len(pairs) >= 1:
        # If only one, return flat pair; if multiple, return list of pairs
        if len(pairs) == 1:
            return [pairs[0][0], pairs[0][1]]
        return [[a, b] for a, b in pairs]
    # Fallback: grab all times mentioned with 's' and pair them in order
    times = re.findall(r"([0-9]+(?:\.[0-9]+)?)\s*s\b", text, flags=re.IGNORECASE)
    if len(times) >= 2:
        if len(times) == 2:
            return [times[0], times[1]]
        # Pair consecutively: (0,1), (2,3), ...
        grouped = []
        for i in range(0, len(times) - 1, 2):
            grouped.append([times[i], times[i+1]])
        return grouped if grouped else [times[0], times[1]]
    raise ValueError("Could not extract t1,t2 for prob0206a")


def kn0214a(html_or_text: str) -> List[str]:
    """Extract x0, vmax, t_total, t_query from Knight 0214a wording (numbers present in text)."""
    text = html_or_text
    x0 = re.search(fr"x\s*0\s*=\s*({DEC_NUM_RE})\s*m", text, flags=re.IGNORECASE)
    vmax = re.search(fr"v\s*max\s*=\s*({DEC_NUM_RE})\s*m\s*/\s*s", text, flags=re.IGNORECASE)
    ttot = re.search(fr"t\s*total\s*=\s*({DEC_NUM_RE})\s*s", text, flags=re.IGNORECASE)
    tq = re.search(fr"t\s*=\s*({DEC_NUM_RE})\s*s\?", text, flags=re.IGNORECASE)
    # More lenient fallback: capture the four numbers in order 6.34, 39.6, 23.1, 15.4
    if not (x0 and vmax and ttot and tq):
        nums = re.findall(fr"{DEC_NUM_RE}", text)
        if len(nums) >= 4:
            return [nums[0], nums[1], nums[2], nums[3]]
        raise ValueError("Could not extract variables for kn0214a")
    return [x0.group(1), vmax.group(1), ttot.group(1), tq.group(1)]


def kn0224a(html_or_text: str) -> List[str]:
    """Extract v0_ms, theta_deg, vf_ms from Knight 0224a wording."""
    text = html_or_text
    v0 = re.search(fr"([0-9]+(?:\.[0-9]+)?)\s*m\s*/\s*s", text, flags=re.IGNORECASE)
    theta = re.search(fr"([0-9]+(?:\.[0-9]+)?)\s*°|([0-9]+(?:\.[0-9]+)?)\s*deg", text, flags=re.IGNORECASE)
    vf = re.findall(fr"([0-9]+(?:\.[0-9]+)?)\s*m\s*/\s*s", text, flags=re.IGNORECASE)
    if not v0 or not theta or len(vf) < 2:
        raise ValueError("Could not extract variables for kn0224a")
    theta_val = theta.group(1) or theta.group(2)
    return [v0.group(1), theta_val, vf[-1]]



def kn0250a(html_or_text: str) -> List[str]:
    """Extract v0_ms, d_m, t_reaction_s from braking problem."""
    text = html_or_text
    # Initial speed: e.g., 18.9 m/s
    v0 = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*m\s*/\s*s", text, flags=re.IGNORECASE)
    # Distance: e.g., 101.0 m (ensure it's not the 'm' in m/s)
    d = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*m\b(?!\s*/\s*s)", text, flags=re.IGNORECASE)
    # Reaction time: look for the specific phrasing 'reaction time is 0.130 s'
    t_reaction = re.search(r"reaction\s+time\s+is\s*([0-9]+(?:\.[0-9]+)?)\s*s", text, flags=re.IGNORECASE)
    
    if not v0 or not d or not t_reaction:
        raise ValueError("Could not extract variables for kn0250a")
    
    return [v0.group(1), d.group(1), t_reaction.group(1)]


def kn0258(html_or_text: str) -> List[str]:
    """Extract a_ms2, dx_m, t1_s, t2_s from constant acceleration problem."""
    text = html_or_text
    # Acceleration: handle m/s^2, m/s 2, m/s<sup>2</sup> → text becomes 'm/s2' after HTML to text
    a = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*m\s*/\s*s(?:\s*\^?\s*2|2)", text, flags=re.IGNORECASE)
    # Distance: standalone meters, not followed by '/ s'
    dx = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*m\b(?!\s*/\s*s)", text, flags=re.IGNORECASE)
    # Times: t=3.75s and t=5.05s
    times = re.findall(r"t\s*=\s*([0-9]+(?:\.[0-9]+)?)\s*s", text, flags=re.IGNORECASE)
    
    if not a or not dx or len(times) < 2:
        raise ValueError("Could not extract variables for kn0258")
    
    return [a.group(1), dx.group(1), times[0], times[1]]


def kn0266a(html_or_text: str) -> List[str]:
    """Extract v_ms, r_m from circular motion problem."""
    text = html_or_text
    # Velocity: e.g., 8.0 m/s
    v = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*m\s*/\s*s", text, flags=re.IGNORECASE)
    # Radius: meters value not followed by / s
    r = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*m\b(?!\s*/\s*s)", text, flags=re.IGNORECASE)
    
    if not v or not r:
        raise ValueError("Could not extract variables for kn0266a")
    
    return [v.group(1), r.group(1)]


def kn0266a_bridge(html_or_text: str) -> List[str]:
    """Extract h_m, v0_ms from the bridge two-rock problem."""
    text = html_or_text
    h = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*m\s+above\s+a\s*river", text, flags=re.IGNORECASE)
    v0 = re.search(r"with\s+a\s*speed\s+of\s*([0-9]+(?:\.[0-9]+)?)\s*m\s*/\s*s", text, flags=re.IGNORECASE)
    if not h or not v0:
        # Fallback: first two numbers in the sentence
        nums = re.findall(r"[0-9]+(?:\.[0-9]+)?", text)
        if len(nums) >= 2:
            return [nums[0], nums[1]]
        raise ValueError("Could not extract variables for kn0266a (bridge)")
    return [h.group(1), v0.group(1)]


def sb0342(html_or_text: str) -> List[str]:
    """Extract m (magnitude of A and B), sum_y (j component magnitude) for sb-prob0342."""
    text = html_or_text
    m = re.search(r"equal\s+magnitudes\s+of\s*([0-9]+(?:\.[0-9]+)?)", text, flags=re.IGNORECASE)
    sumj = re.search(r"vector\s+([0-9]+(?:\.[0-9]+)?)\s*\bj\b", text, flags=re.IGNORECASE)
    if not m or not sumj:
        raise ValueError("Could not extract variables for sb0342")
    return [m.group(1), sumj.group(1)]


def sb0353(html_or_text: str) -> List[str]:
    """Extract k ratio (|A+B| is k times |A-B|) for sb-prob0353."""
    text = html_or_text
    k = re.search(r"be\s*([0-9]+(?:\.[0-9]+)?)\s*times\s+greater\s+than\s+the\s+magnitude\s+of\s*A\s*[-]\s*B", text, flags=re.IGNORECASE)
    if not k:
        # Fallback: first number in the sentence
        k2 = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*times", text, flags=re.IGNORECASE)
        if not k2:
            raise ValueError("Could not extract ratio for sb0353")
        return [k2.group(1)]
    return [k.group(1)]


def sb0416a(html_or_text: str) -> List[str]:
    """Extract v0_ms, theta_deg (below horizontal), t_s for sb-prob0416a."""
    text = html_or_text
    v0 = re.search(r"initial\s+velocity\s+of\s*([0-9]+(?:\.[0-9]+)?)\s*m\s*/\s*s", text, flags=re.IGNORECASE)
    theta = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*(?:°|deg)\s+below\s+the\s+horizontal", text, flags=re.IGNORECASE)
    t = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*s\s+later", text, flags=re.IGNORECASE)
    if not v0 or not theta or not t:
        raise ValueError("Could not extract variables for sb0416a")
    return [v0.group(1), theta.group(1), t.group(1)]


def sb0344(html_or_text: str) -> List[str]:
    """Extract three legs: d1, ang1_deg, d2, ang2_deg, d3, ang3_deg."""
    text = html_or_text
    # Distances and angles appear as: 68.0 paces at 237deg, ... 133 paces, ... 110 paces at 160deg
    ds = re.findall(r"([0-9]+(?:\.[0-9]+)?)\s*paces", text, flags=re.IGNORECASE)
    angs = re.findall(r"([0-9]+(?:\.[0-9]+)?)\s*(?:°|deg)\b", text, flags=re.IGNORECASE)
    if len(ds) < 3 or len(angs) < 3:
        raise ValueError("Could not extract variables for sb0344")
    return [ds[0], angs[0], ds[1], angs[1], ds[2], angs[2]]


REGISTRY: Dict[str, Callable[[str], List[str]]] = {
    "prob1508": prob1508,
    "prob1514": prob1514,
    "prob1560a": prob1560a,
    "prob0210a": prob0210a,
    "prob0218": prob0218,
    "prob0246": prob0246,
    "prob0258": prob0258,
    "prob0206a": prob0206a,
    "kn0214a": kn0214a,
    "kn0224a": kn0224a,
    "kn0250a": kn0250a,
    "kn0258": kn0258,
    "kn0266a": kn0266a,
    "kn0266a_bridge": kn0266a_bridge,
    "sb0342": sb0342,
    "sb0353": sb0353,
    "sb0416a": sb0416a,
    "sb0344": sb0344,
}


def sb0441a(html_or_text: str) -> List[str]:
    """Extract v_current_kmh, d_cross_km, d_up_km, v_boat_kmh for river rescue problem."""
    text = html_or_text
    # Grab all speeds that look like km/h in order of appearance (current first, boat second)
    speeds = re.findall(r"([0-9]+(?:\.[0-9]+)?)\s*km\s*/\s*h", text, flags=re.IGNORECASE)
    vcur = speeds[0] if len(speeds) >= 1 else None
    vboat = speeds[1] if len(speeds) >= 2 else None

    # Distances: cross-river (from shore) and upstream distance
    dcross_m = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*km\s*from\s*shore", text, flags=re.IGNORECASE)
    dup_m = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*km\s*upstream", text, flags=re.IGNORECASE)

    # Fallback: if phrasing slightly differs, take first two km numbers as they appear: from shore then upstream
    if (dcross_m is None or dup_m is None):
        km_numbers = re.findall(r"([0-9]+(?:\.[0-9]+)?)\s*km\b", text, flags=re.IGNORECASE)
        if dcross_m is None and len(km_numbers) >= 1:
            class _M:  # tiny helper to mimic group access
                def __init__(self, v): self._v = v
                def group(self, i): return self._v
            dcross_m = _M(km_numbers[0])
        if dup_m is None and len(km_numbers) >= 2:
            class _M2:
                def __init__(self, v): self._v = v
                def group(self, i): return self._v
            dup_m = _M2(km_numbers[1])

    if not (vcur and vboat and dcross_m and dup_m):
        raise ValueError("Could not extract variables for sb0441a")

    return [vcur, dcross_m.group(1), dup_m.group(1), vboat]


def sb0464(html_or_text: str) -> List[str]:
    """Extract x0_km, t_up_min from river-log timing problem."""
    text = html_or_text
    # Distance traveled upstream before passing the log
    x0 = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*km\s*upstream", text, flags=re.IGNORECASE)
    # Upstream time before turning around and meeting the log later
    tmin = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*min\b", text, flags=re.IGNORECASE)

    # Fallbacks: pick first km number and first minutes number in the sentence
    if x0 is None:
        x0_list = re.findall(r"([0-9]+(?:\.[0-9]+)?)\s*km\b", text, flags=re.IGNORECASE)
        if len(x0_list) >= 1:
            class _MX:
                def __init__(self, v): self._v = v
                def group(self, i): return self._v
            x0 = _MX(x0_list[0])
    if tmin is None:
        t_list = re.findall(r"([0-9]+(?:\.[0-9]+)?)\s*(?:min|minutes)\b", text, flags=re.IGNORECASE)
        if len(t_list) >= 1:
            class _MT:
                def __init__(self, v): self._v = v
                def group(self, i): return self._v
            tmin = _MT(t_list[0])

    if not (x0 and tmin):
        raise ValueError("Could not extract variables for sb0464")
    return [x0.group(1), tmin.group(1)]


def sb0446(html_or_text: str) -> List[str]:
    """Extract r_m, h_m, R_m from circular-break projectile problem."""
    text = html_or_text
    # Primary patterns
    r = re.search(r"radius\s*([0-9]+(?:\.[0-9]+)?)\s*m\b", text, flags=re.IGNORECASE)
    h = re.search(r"plane\s*of\s*the\s*circle\s*is\s*([0-9]+(?:\.[0-9]+)?)\s*m\s*above\s*the\s*ground", text, flags=re.IGNORECASE)
    R = re.search(r"lands\s*([0-9]+(?:\.[0-9]+)?)\s*m\s*(?:\(horizontally\)\s*)?away", text, flags=re.IGNORECASE)

    # Fallbacks: find three meter values in order radius, height above ground, horizontal distance
    if not (r and h and R):
        m_vals = re.findall(r"([0-9]+(?:\.[0-9]+)?)\s*m\b", text, flags=re.IGNORECASE)
        if len(m_vals) >= 3:
            class _M:
                def __init__(self, v): self._v = v
                def group(self, i): return self._v
            if r is None: r = _M(m_vals[0])
            if h is None: h = _M(m_vals[1])
            if R is None: R = _M(m_vals[2])

    if not (r and h and R):
        raise ValueError("Could not extract variables for sb0446")
    return [r.group(1), h.group(1), R.group(1)]


def hr0483(html_or_text: str) -> List[str]:
    """Extract v_air_kmh, distance_km, heading_deg_east_of_north, time_hr. Flexible units."""
    text = html_or_text
    # Allow km/h or km/hr
    v_air = re.search(r"airspeed\s*of\s*([0-9]+(?:\.[0-9]+)?)\s*km\s*/\s*h(?:r)?\b", text, flags=re.IGNORECASE)
    # Distance along north direction
    dist = re.search(r"fly\s*([0-9]+(?:\.[0-9]+)?)\s*km\s*(?:to\s*the\s*north|due\s*north)", text, flags=re.IGNORECASE)
    # Heading in degrees east of north
    heading = re.search(r"head\s*([0-9]+(?:\.[0-9]+)?)\s*(?:°|deg)\s*east\s*of\s*north", text, flags=re.IGNORECASE)
    # Time in hours
    time = re.search(r"arrives\s*in\s*([0-9]+(?:\.[0-9]+)?)\s*h(?:r|ours)?\b", text, flags=re.IGNORECASE)

    # Fallbacks by units
    if v_air is None:
        v_list = re.findall(r"([0-9]+(?:\.[0-9]+)?)\s*km\s*/\s*h(?:r)?\b", text, flags=re.IGNORECASE)
        if len(v_list) >= 1:
            class _MV: 
                def __init__(self, v): self._v = v
                def group(self, i): return self._v
            v_air = _MV(v_list[0])
    if dist is None:
        d_list = re.findall(r"([0-9]+(?:\.[0-9]+)?)\s*km\b", text, flags=re.IGNORECASE)
        if len(d_list) >= 1:
            class _MD:
                def __init__(self, v): self._v = v
                def group(self, i): return self._v
            dist = _MD(d_list[0])
    if heading is None:
        head_list = re.findall(r"([0-9]+(?:\.[0-9]+)?)\s*(?:°|deg)\b", text, flags=re.IGNORECASE)
        if len(head_list) >= 1:
            class _MH:
                def __init__(self, v): self._v = v
                def group(self, i): return self._v
            heading = _MH(head_list[0])
    if time is None:
        t_list = re.findall(r"([0-9]+(?:\.[0-9]+)?)\s*h(?:r|ours)?\b", text, flags=re.IGNORECASE)
        if len(t_list) >= 1:
            class _MT:
                def __init__(self, v): self._v = v
                def group(self, i): return self._v
            time = _MT(t_list[0])

    if not (v_air and dist and heading and time):
        raise ValueError("Could not extract variables for hr0483")
    return [v_air.group(1), dist.group(1), heading.group(1), time.group(1)]

REGISTRY.update({
    "sb0441a": sb0441a,
    "sb0464": sb0464,
    "sb0446": sb0446,
    "hr0483": hr0483,
})
