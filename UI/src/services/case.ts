import {api} from 'boot/axios'
import {ref} from 'vue';
import {showSuccessNotify, showErrorNotify} from '../common/utils';

function Case() {

  const dialogEdit = ref<boolean>(false);

  const columns = [
    {name: 'id', label: 'ID', field: 'id'},
    {name: 'case_name', label: '规则方案', field: 'case_name', align: 'left'},
    {name: 'short_circuit', label: '短路', field: 'short_circuit', align: 'center'},
    {name: 'blank_skip', label: '空值跳过', field: 'blank_skip', align: 'center'},
    {name: 'create_time', label: '创建时间', field: 'create_time'},
    {name: 'update_time', label: '修改时间', field: 'update_time'},
    {name: 'handle', label: '操作', field: 'handle'},
  ];
  const rows = ref<Array<object>>();
  const loadList = (params?: object) => {
    api.get('/api/case/').then(
      res => {
        rows.value = res.data
      }
    );
  };
  const saveItem = (params: object) => {
    if ('id' in params) {
      api.put(`/api/case/${params.id}/`, params).then((res) => {
        showSuccessNotify('保存成功');
        loadList();
        dialogEdit.value = false;
      }).catch(error => {
        console.log(error.response.data.blank_skip);
        showErrorNotify(error.response.data.blank_skip);

      });
    } else {
      api.post('/api/case/', params).then((res) => {
        showSuccessNotify('保存成功');
        loadList()
        dialogEdit.value = false;
      }).catch(error => {
        showErrorNotify(error.response.data.blank_skip);
      });
    }

  };

  const deleteItem = (id: number) => {
    api.delete(`/api/case/${id}/`).then((res) => {
      showSuccessNotify('保存成功');
      loadList()
    }).catch(error => {
      showErrorNotify(error.response.data.blank_skip);
    });
  };

  return {dialogEdit, columns, rows, loadList, saveItem, deleteItem}
}

export {Case}
