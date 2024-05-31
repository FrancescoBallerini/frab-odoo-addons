# ListView Make All Fields Optional

## Description

<div style="font-size:14px;">

This module has been designed to allow more flexibility in the process of manipulating
fields visibility through the optional fields dropdown menu that you can find on the
right side of list-views.

The problem with this feature is that fields will not appear in the optional dropdown
menu unless they have been explicitly assigned the attribute 'optional', which might be
hard to do for non-technical users, or a big waste of time even for technical /
developers, expecially considering the fact that this attribute is rarely added by odoo
developers themselves, and you will need to inherit the whole module and view even to
set a single field to optional.

This module will solve this issue by ALWAYS applying the attribute 'optional' to all
fields defined in the list-view. User can simply hide fields that he don't want to see.

Besides 'optional' attribute, the static 'visibility' attributes and group restrictions
will still be applied to the columns (those columns will still not appear in the
dropdown).

## Details

Specifically the module will implement the following behaviour to all list-views and x2m
list-views:

<ul>
    <li>
        all fields defined in the list without the 'optional' attribute will gain the 'optional' attribute set on 'show':
        This basically means that those fields still visible but can be hidden
    </li>
    <li>
        all fields defined in the list with 'optional' attributes set to 'show' will be kept as is
    </li>
    <li>
        all fields defined in the list with 'optional' attributes set to 'hide' will be kept as is
    </li>
    <li>
        if a user cannot see the column (field) due to group restrictions, he will not be able the field in the optional dropdown menu
    </li>
    <li>
        besides its 'optional' attribute declaration, if the column is explicitly flagged as 'invisible', it will not be shown
        in the optional dropdown menu
    </li>
</ul>
</div>
