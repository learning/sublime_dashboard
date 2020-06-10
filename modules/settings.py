import os
import json

import sublime

default_settings = {'color_scheme': 'Monokai.sublime-color-scheme', 'font_face': '', 'font_size': 10, 'font_options': [], 'theme_font_options': [], 'word_separators': './\\()"\'-:,.;<>~!@#$%^&*|+=[]{}`~?', 'line_numbers': True, 'gutter': True, 'margin': 4, 'fold_buttons': True, 'fade_fold_buttons': True, 'mini_diff': True, 'rulers': [], 'spell_check': False, 'tab_size': 4, 'translate_tabs_to_spaces': False, 'use_tab_stops': True, 'detect_indentation': True, 'auto_indent': True, 'smart_indent': True, 'indent_to_bracket': False, 'trim_automatic_white_space': True, 'word_wrap': 'auto', 'wrap_width': 0, 'indent_subsequent_lines': True, 'draw_centered': False, 'auto_match_enabled': True, 'dictionary': 'Packages/Language - English/en_US.dic', 'spelling_selector': 'markup.raw, source string.quoted - punctuation - meta.preprocessor.include, source comment - source comment.block.preprocessor, -(source, constant, keyword, storage, support, variable, markup.underline.link, meta.tag)', 'draw_minimap_border': False, 'always_show_minimap_viewport': False, 'highlight_line': False, 'caret_style': 'smooth', 'caret_extra_top': 2, 'caret_extra_bottom': 2, 'caret_extra_width': 1, 'block_caret': False, 'match_brackets': True, 'match_brackets_content': True, 'match_brackets_square': True, 'match_brackets_braces': True, 'match_brackets_angle': False, 'match_tags': True, 'match_selection': True, 'line_padding_top': 0, 'line_padding_bottom': 0, 'scroll_past_end': True, 'move_to_limit_on_up_down': False, 'draw_white_space': 'selection', 'draw_indent_guides': True, 'indent_guide_options': ['draw_normal'], 'trim_trailing_white_space_on_save': False, 'ensure_newline_at_eof_on_save': False, 'save_on_focus_lost': False, 'atomic_save': False, 'fallback_encoding': 'Western (Windows 1252)', 'default_encoding': 'UTF-8', 'enable_hexadecimal_encoding': True, 'default_line_ending': 'system', 'show_definitions': True, 'tab_completion': True, 'auto_complete': True, 'auto_complete_size_limit': 4194304, 'auto_complete_delay': 50, 'auto_complete_selector': 'meta.tag - punctuation.definition.tag.begin, source - comment - string.quoted.double.block - string.quoted.single.block - string.unquoted.heredoc', 'auto_complete_triggers': [{'selector': 'text.html', 'characters': '<'}], 'auto_complete_commit_on_tab': False, 'auto_complete_with_fields': False, 'auto_complete_cycle': False, 'auto_close_tags': True, 'shift_tab_unindent': False, 'copy_with_empty_selection': True, 'find_selected_text': True, 'auto_find_in_selection': False, 'drag_text': True, 'theme': 'Default.sublime-theme', 'scroll_speed': 1, 'tree_animation_enabled': True, 'animation_enabled': True, 'highlight_modified_tabs': False, 'show_tab_close_buttons': True, 'bold_folder_labels': False, 'adaptive_dividers': True, 'gpu_window_buffer': 'auto', 'native_tabs': 'system', 'overlay_scroll_bars': 'system', 'enable_tab_scrolling': True, 'show_encoding': False, 'show_line_endings': False, 'ui_scale': 0, 'hot_exit': True, 'remember_full_screen': False, 'shell_environment': True, 'always_prompt_for_file_reload': False, 'open_files_in_new_window': True, 'create_window_at_startup': True, 'show_navigation_bar': True, 'close_windows_when_empty': False, 'show_full_path': True, 'show_panel_on_build': True, 'show_errors_inline': True, 'show_git_status': True, 'allow_git_home_dir': False, 'git_diff_target': 'index', 'preview_on_click': True, 'folder_exclude_patterns': ['.svn', '.git', '.hg', 'CVS'], 'file_exclude_patterns': ['*.pyc', '*.pyo', '*.exe', '*.dll', '*.obj', '*.o', '*.a', '*.lib', '*.so', '*.dylib', '*.ncb', '*.sdf', '*.suo', '*.pdb', '*.idb', '.DS_Store', '*.class', '*.psd', '*.db', '*.sublime-workspace'], 'binary_file_patterns': ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.ttf', '*.tga', '*.dds', '*.ico', '*.eot', '*.pdf', '*.swf', '*.jar', '*.zip'], 'index_files': True, 'index_workers': 0, 'index_exclude_patterns': ['*.log'], 'ignored_packages': ['Vintage']}

def settings(data):
  filename = os.path.join(sublime.packages_path(), 'User', 'Preferences.sublime-settings')
  try:
    f = open(filename, 'r')

    fs = os.fstat(f.fileno())
    # user's settings, a python dict
    fdict = json.loads(f.read(fs.st_size))
    f.close()

    if data:
      # update settings
      data = json.loads(data.decode('utf-8'))

      for k in data.keys():
        # TODO: array/list compare
        if data.get(k) is default_settings.get(k):
          fdict.pop(k, None)
        else:
          fdict[k] = data.get(k)

      out = open(filename, 'wb')
      indent = fdict.get('tab_size', default_settings.get('tab_size', 4))
      out.write(json.dumps(fdict, indent=indent).encode('utf-8'))
      out.close()
      result = {
        'error': 0
      }
    else:
      # get settings
      result = {
        'error': 0,
        'data': fdict
      }
    return result
  except Exception as e:
    return {
      'error': 1,
      'message': str(e)
    }

