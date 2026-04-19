def sol(gain: list[int]) -> int:
    psum = 0
    m = 0

    for i in gain:
        psum += i
        if psum > m:
            m = psum

    return m