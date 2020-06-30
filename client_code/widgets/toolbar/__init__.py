from ._anvil_designer import toolbarTemplate
from anvil import *

class toolbar(toolbarTemplate):
  
  def __init__(self, align, section, parent, **properties):

    self.init_components(**properties)
    
    self.tag.parent=parent
    self.tag.is_section=section == parent
    self.tag.section=section
    self.tag.parent=parent
    self.link_down.tag.direction=1
    self.link_up.tag.direction=-1
    
    if align=='center':
      self.flow_panel.align='center'
   
  def remove_parent(self, **event_args):
    self.tag.parent.remove_from_parent()
    
    if not self.tag.is_section:
      get_open_form().color_rows()
      
  def move_widget(self, **event_args):
    
    direction=event_args['sender'].tag.direction
    
    if not self.tag.is_section:
        
      comp=self.tag.parent
      section=self.tag.section
      items=section.column_panel.get_components()
      ind=items.index(comp)
      
      if (ind>0 and direction==-1) or (ind<len(items)-1 and direction==1):
        items[ind+direction], items[ind] = items[ind], items[ind+direction]
        section.column_panel.clear()
        [section.column_panel.add_component(item) for item in items]
        
    else:
      
      comp=self.tag.parent
      section=get_open_form()
      items=section.content_panel.get_components()
      print(type(items[0]))
      print(type(comp))
      ind=items.index(comp)
      print(ind)
      
      if (ind>0 and direction==-1) or (ind<len(items)-1 and direction==1):
        items[ind+direction], items[ind] = items[ind], items[ind+direction]
        section.content_panel.clear()
        [section.content_panel.add_component(item) for item in items]
      
      
      
      
      

