import {api} from 'boot/axios'
import {ref} from 'vue';
import {showSuccessNotify, showErrorNotify} from '../common/utils';

function CaseVersion() {

  const path = '/api/version/';
  const dialogEdit = ref<boolean>(false);

  const columns = [
    {name: 'id', label: 'ID', field: 'id', hidden:true},
    {name: 'version_name', label: '版本名', field: 'version_name', align: 'left'},
    {name: 'version_code', label: '版本号', field: 'version_code'},
    {name: 'version_default', label: '默认', field: 'version_default'},
    {name: 'create_time', label: '创建时间', field: 'create_time'},
    {name: 'update_time', label: '修改时间', field: 'update_time'},
    {name: 'handle', label: '操作', field: 'handle', required:true},
  ];
  const rows = ref<Array<object>>();
  const loadList = (params?: object) => {
    api.get(path).then(
      res => {
        rows.value = res.data
      }
    );
  };
  const saveItem = (params: object) => {
    if ('id' in params) {
      api.put(`${path}${params.id}/`, params).then((res) => {
        showSuccessNotify('保存成功');
        loadList();
        dialogEdit.value = false;
      }).catch(error => {

        showErrorNotify(error.response.data);

      });
    } else {
      api.post(path, params).then((res) => {
        showSuccessNotify('保存成功');
        loadList()
        dialogEdit.value = false;
      }).catch(error => {
        showErrorNotify(error.response.data);
      });
    }

  };

  return {dialogEdit, columns, rows, loadList, saveItem}
}

export {CaseVersion}
