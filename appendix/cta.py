"""
Context Transformation Algorithm (c) 2008-2024 <yauhen.yakimovich.mail@gmail.com>
require: bitarray==2.7.3
"""
from bitarray import bitarray as ba


def cta(in_bits, cxt_size=4):
    """Context transformation algorithm function."""
    if type(in_bits) != ba:
        in_bits = ba(in_bits)
    out_bits = ba()
    # initiate context lookup by setting current states to zeros
    lookup = ba([False for x in range(2 << cxt_size)])
    cxt = ba([False for x in range(cxt_size)])
    for x in in_bits:
        index = int(cxt.to01(), 2)
        state = lookup[index]
        # output '1' to signal a change of state,
        # otherwise output '0'
        diff = state != x
        out_bits.append(diff)
        # update last remembered state in lookup
        if diff:
            lookup[index] = x
        cxt.pop(0)
        cxt.append(x)
    return out_bits


def inv_cta(in_bits, cxt_size=4):
    """Inverse context transformation algorithm function."""
    if type(in_bits) != ba:
        in_bits = ba(in_bits)
    out_bits = ba()
    # initiate context lookup by setting current states to zeros
    lookup = ba([False for x in range(2 << cxt_size)])
    cxt = ba([False for x in range(cxt_size)])
    for x in in_bits:
        index = int(cxt.to01(), 2)
        state = lookup[index]
        # inverse: output original value and reconstruct
        #          the state lookup table
        if not x:
            # since state was not changed - pick the value
            # from the context state
            v = state
        else:
            # state was changed by the original transformation
            # - output value will be an inverse of state
            v = not(state)
        out_bits.append(v)
        lookup[index] = v
        # update current context
        cxt.pop(0)
        cxt.append(v)
    return out_bits


def assert_cta():
    """
    Test direct and inverse CTA mapping.

    Output:

        bitarray('101001110111011111011111111111110')
        bitarray('101001110111000011100001000000001')
        bitarray('101001110111011111011111111111110')
    """
    pre_image = '101001110111011111011111111111110'
    image = cta(pre_image)
    print(ba(pre_image))
    print(image)
    print(inv_cta(image))
    assert ba(pre_image) == inv_cta(image)


if __name__ == '__main__':
    assert_cta()
