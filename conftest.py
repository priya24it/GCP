import pytest

# def pytest_collection_modifyitems(items):
#     """test items come to first"""
#     run_first = ["test_abcd.TestSample.test_count", "test_abcd.TestSample.test_compare"]
#     modules = {item: item.module.__name__ for item in items}
#     items[:] = sorted(
#         items, key=lambda x: run_first.index(modules[x]) if modules[x] in run_first else len(items)
#     )


def pytest_collection_modifyitems(config, items):
    """Modifies test items in place to ensure test modules run in a given order"""
    def param_part(item):
        # logger.info(item.nodeid)
        if item.nodeid.startswith("test_abcd.py::TestSample::"):
            index_param_value = item.nodeid.find('[')
            if index_param_value > 0:
                tb_param_name = item.nodeid[item.nodeid.index('['):]
                test_name = item.nodeid[item.nodeid.index('::test_')+2:item.nodeid.index('[')]
                if tb_param_name.find('-') > 0:
                    tb_name = tb_param_name[:tb_param_name.index('-')] + "]"
                    param_name = tb_param_name[tb_param_name.index('-'):tb_param_name.index(']')]
                else:
                    tb_name = tb_param_name
                    param_name = ""
                item_final_name = tb_name + '::' + test_name + '::' + param_name
                return item_final_name
        return item.nodeid

    items[:] = sorted(items, key=param_part)