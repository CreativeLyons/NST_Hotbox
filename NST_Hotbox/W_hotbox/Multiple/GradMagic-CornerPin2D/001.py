#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Link CornerPin
# COLOR: #5a892b
# TEXTCOLOR: #ffffff
#
#----------------------------------------------------------------------------------------------------------

import nukescripts

ns = nuke.selectedNodes()

nukescripts.clear_selection_recursive()
gradMagics = []
for n in ns:
    if n.Class() == "CornerPin2D":
        n.knob('selected').setValue(True)
    else:
        gradMagics.append(n)

for n in gradMagics:
    n.knob('linkCornerPin').execute()
