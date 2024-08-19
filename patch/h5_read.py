import h5py

h5_path = 'Visium_FFPE_Human_Breast_Cancer_filtered_feature_bc_matrix (1).h5'
with h5py.File(h5_path, 'r') as hdf:
    # 查看文件中的数据集名称
    def print_attrs(name, obj):
        print(name)
        for key, val in obj.attrs.items():
            print("    %s: %s" % (key, val))




    hdf.visititems(print_attrs)
    spot_ids = hdf['matrix/features/feature_type'][:]
    print(spot_ids)