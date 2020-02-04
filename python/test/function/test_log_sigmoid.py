# Copyright (c) 2017 Sony Corporation. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
import numpy as np
import nnabla.functions as F
from nbla_test_utils import list_context

ctxs = list_context('LogSigmoid')


def ref_log_sigmoid(x):
    return np.log(1 / (1 + np.exp(-x, dtype=x.dtype)))


@pytest.mark.parametrize("ctx, func_name", ctxs)
@pytest.mark.parametrize("seed", [313])
def test_log_sigmoid_forward_backward(seed, ctx, func_name):
    from nbla_test_utils import cap_ignore_region, function_tester
    rng = np.random.RandomState(seed)
    inputs = [
        np.clip(np.abs(rng.randn(2, 3, 4).astype(np.float32)) * 1e4, 1e-2, 1e4)]
    function_tester(rng, F.log_sigmoid, ref_log_sigmoid, inputs,
                    ctx=ctx, func_name=func_name)


@pytest.mark.parametrize("ctx, func_name", ctxs)
@pytest.mark.parametrize("seed", [313])
def test_log_sigmoid_double_backward(seed, ctx, func_name):
    from nbla_test_utils import cap_ignore_region, backward_function_tester
    rng = np.random.RandomState(seed)
    inputs = [
        np.clip(np.abs(rng.randn(2, 3, 4).astype(np.float32)) * 1e4, 1e-2, 1e4)]
    backward_function_tester(rng, F.log_sigmoid, None,
                             inputs=inputs,
                             func_args=[], func_kwargs={},
                             atol_b=1e-3,
                             atol_accum=1e-3,
                             dstep=1e-3,
                             ctx=ctx, func_name=None,
                             disable_half_test=False)
