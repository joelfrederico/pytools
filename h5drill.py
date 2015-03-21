import h5py as _h5

__all__ = ['H5Drill']


class H5Drill(object):
    def __init__(self, data):
        self._hdf5 = data
        #  self._mydir = []
        for key in data.keys():
            if key[0] != '#':
                #  self._mydir.append(key)
                out = data[key]
                if type(out) == _h5._hl.group.Group:
                    setattr(self, key, H5Drill(data[key]))
                elif len(out.shape) == 2:
                    if out.shape[0] == 1 or out.shape[1] == 1:
                        out = out.value.flatten()
                    setattr(self, key, out)
                elif key == 'UID':
                    setattr(self, key, data[key].value)
                # elif key == 'dat':
                #     uids = data['UID'].value
                #     dats = E200_api_getdat(data, uids)
                #     setattr(self, key, dats.dat)
                else:
                    setattr(self, key, data[key])

    def __repr__(self):
        out = '\<E200.E200_load_data.Drill with keys:\n_hdf5'
        for val in self._hdf5.keys():
            out = out + '\n' + val

        out = out[1:] + '\n>'
        return out
