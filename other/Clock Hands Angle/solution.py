def clock_hands_angle(hour, minute):
    # 60 min in 360 deg -> 6 deg per minute
    # 12 h in 360 deg -> 30 deg per hour
    m_deg = minute * 6

    # consider hour hand shift
    h_deg = hour * 30 + (minute / 60) * 30

    dif = abs(h_deg - m_deg)

    return (360 - dif) if dif > 360 else dif


deg = clock_hands_angle(8, 15)
print(deg)
