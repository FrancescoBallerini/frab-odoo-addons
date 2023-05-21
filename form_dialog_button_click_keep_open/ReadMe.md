## Form Dialog: keep open on button click

In Odoo Backend, as default, when you open an action window in a Dialog / FormViewDialog (non full-screen mode), as soon as you click on a button the dialog will close automatically.

The standard workaround to avoid this behaviour is pretty simple: you can just return another action of type 'ir.actions.act_window' with same id as the current record, target new (will re-open dialog instead of full-screen),
and it will basically requires to write a code similar to this:

```
view_id = self.sudo().get_formview_id(access_uid=access_uid)
# re-open current record in a dialog:
return {
    'type': 'ir.actions.act_window',
    'res_model': self._name,
    'view_type': 'form',
    'view_mode': 'form',
    'views': [(view_id, 'form')],
    'target': 'new',
    'res_id': self.id,
    'context': dict(self._context),
}
```
This module will avoid you to write this code. 

## Usage
After module installation you can use class ```o_btn_keep_open``` on your buttons.

```
<button type='object' name='my_button' class='o_btn_keep_open'/>
```

By using this class selector you will achieve the same result than you would achieve by returning the action in python: it will keep dialog open when you click on 'my_button'. 


## Other infos
You can also use another class selector ```o_btn_reopen``` , which leads to a slightly different behaviour. 

The difference is that it will actually ends the native process (close dialog) and then re-open it, while 'o_btn_keep_open' 
will avoid closing<b>*</b> the dialog. 

Aniway, I <b>hardly</b> suggest using ```o_btn_keep_open``` since it will avoid the annoying animation due to the dialog closing and re-opening. 

Note that this is litterally the same than returning the action in python, it will not allow you to stack more than one action, just a shortcut.

<span><b>*</b></span> May be a non existent difference for the user, but it's probably worth mentioning what really happens in background: when a button is click the dialog is always closed, no matter what (also if
you return the action in python). What happens in this case, is that a new dialog is firstly opened, then second dialog is destroyed in background.
This is an efficient way for the js-framework to fully update the view status (e.g. field widget values) while also keeping UI responsive, because the user feels like the dialog never close : ) 

Note that it means that you will, for example, lose the reference to the scroll position if you have a "long dialog".
 

