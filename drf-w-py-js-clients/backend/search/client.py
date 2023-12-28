from algoliasearch_django import algolia_engine


def get_client():
    return algolia_engine.client


def get_index(index_name="hk_Product"):
    client = get_client()
    index = client.init_index(index_name)
    return index


def get_index_names(index_names="hk_Product, hk_Article"):
    return [index_name.strip() for index_name in index_names.split(",")]


def perform_search(query, *args, **kwargs):
    index = get_index()
    params = {}
    tags = ""
    if "tags" in kwargs:
        tags = kwargs.pop("tags") or []
        if len(tags) != 0:
            params["tagFilters"] = tags
    index_filters = [f"{k}:{v}" for k, v in kwargs.items() if v != ""]
    if len(index_filters) != 0:
        params["facetFilters"] = index_filters

    results = index.search(query, params)
    return results


def create_params_from_kwargs(**kwargs):
    params = {}
    tags = ""
    if "tags" in kwargs:
        tags = kwargs.pop("tags") or []
        if len(tags) != 0:
            params["tagFilters"] = tags
    index_filters = [f"{k}:{v}" for k, v in kwargs.items() if v != ""]
    if len(index_filters) != 0:
        params["facetFilters"] = index_filters
    return params


def perform_search_on_multiple_indices(query, index_names="", **kwargs):
    index_names = (
        get_index_names() if len(index_names) == 0 else get_index_names(index_names)
    )
    all_results = {}
    for index_name in index_names:
        index = get_index(index_name)

        if "public" in kwargs and kwargs.get("public") == True:
            if index_name != "hk_Article":
                params = create_params_from_kwargs(**kwargs)
            else:
                kwargs_without_public = {
                    k: v for k, v in kwargs.items() if k != "public" and v != ""
                }
                params = create_params_from_kwargs(**kwargs_without_public)

        else:
            params = create_params_from_kwargs(**kwargs)

        all_results[index_name] = index.search(query, params)
    return all_results
