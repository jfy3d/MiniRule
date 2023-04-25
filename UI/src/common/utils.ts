import { Notify } from 'quasar'
const showNotify = (color:string, message:string, timeout:number) =>{
  Notify.create({
    color:color,
    message:message,
    position:'center',
    timeout:timeout
  });
};

export function showSuccessNotify(message:string){
  showNotify('green', message, 1000);
};

export function showErrorNotify(message:string){
  showNotify('red', message, 2000);
};
