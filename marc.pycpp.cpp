#py from marc import *
#py for cmd in pycpp.params['commands']:
std::vector<msgpack::object>* `cmd.name`(
#py for p in cmd.params:
#py if p.dtype == 'string':
    char *`p.name`_data,
    size_t `p.name`_size,
#py else:
    `p.dtype` `p.name`,
#py endif
#py endfor
    const char* topic
);
#py endfor
