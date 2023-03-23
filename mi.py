from multiprocessing.pool import ThreadPool
from functools import partial
from tqdm import tqdm
import os 
from ctypes import *
from typing import Iterable


# Connecting C++ library
libname = os.path.abspath(os.path.join(os.path.dirname(__file__), "libmi.so"))
mi_lib = CDLL(libname)
mi_lib.mi.restype = c_longdouble


def mi(txts: Iterable[str], tgts: Iterable[str], word: str, tgt: str) -> float:
    """ Wrapper for C++ calculation function.

    This makes converting variables to C++ types, calling C++ function and returning result.

    MI is a non-negative value. It is equal to 0 when random variables are independent.
    In C++ realisation if MI couldn't be calculated the error code is returned. 
    This code is negative.

    params: 
    @txts: Iterable[String]: Iterable of texts
    @tgts: Iterable[String]: Iterable of targets corresponding to texts from @txts.
                             All targets corresponding to one text should be separated by "|".
    @word: String: Word for building Mutual Information for.
    @tgt: String: Target for building mutual information for.

    @result: Float: Mutual Information between @word and @tgt.
    """
    txt_c = (c_char_p * len(txts))()
    tgt_c = (c_char_p * len(tgts))()
    txt_c[:] = [s.encode() for s in txts]
    tgt_c[:] = [s.encode() for s in tgts]

    res = mi_lib.mi(txt_c, len(txts),
                    create_string_buffer(str.encode(tgt)), 
                    tgt_c, create_string_buffer(str.encode(word)))
    return res if res > -1 else None

