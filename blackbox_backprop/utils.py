import ray


def maybe_parallelize(function, arg_list):
    """
    Parallelizes execution is ray is enabled
    :param function: callable
    :param arg_list: list of function arguments (one for each execution)
    :return:
    """
    if ray.is_initialized():
        ray_fn = ray.remote(function)
        return ray.get([ray_fn.remote(arg) for arg in arg_list])
    else:
        return [function(arg) for arg in arg_list]
