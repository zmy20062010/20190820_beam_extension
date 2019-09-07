from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

result00 = sio.loadmat('bm_ext_base_laml_l_00e-3.mat'); 
vplist00  = result00['Vplist'];
result01 = sio.loadmat('bm_ext_base_laml_l_10e-3.mat'); 
vplist01  = result01['Vplist'];
result02 = sio.loadmat('bm_ext_base_laml_l_20e-3.mat'); 
vplist02  = result02['Vplist'];
result03 = sio.loadmat('bm_ext_base_laml_l_30e-3.mat'); 
vplist03  = result03['Vplist'];
result04 = sio.loadmat('bm_ext_base_laml_l_40e-3.mat'); 
vplist04  = result04['Vplist'];
result05 = sio.loadmat('bm_ext_base_laml_l_50e-3.mat'); 
vplist05  = result05['Vplist'];
result06 = sio.loadmat('bm_ext_base_laml_l_60e-3.mat'); 
vplist06  = result06['Vplist'];
result07 = sio.loadmat('bm_ext_base_laml_l_70e-3.mat');
vplist07  = result07['Vplist'];
result08 = sio.loadmat('bm_ext_base_laml_l_80e-3.mat'); 
vplist08  = result08['Vplist'];
result09 = sio.loadmat('bm_ext_base_laml_l_90e-3.mat'); 
vplist09  = result09['Vplist'];
result10 = sio.loadmat('bm_ext_base_laml_l_100e-3.mat'); 
vplist10  = result10['Vplist'];


fr        = result01['fr'];
Rl        = result01['Rl'];
xib       = result01['xib'];

fig2 = plt.figure(2, figsize=(12,8))
plt.plot(fr[0,:],np.abs(vplist00[5,:]),'r', label= '$\lambda_l$=0.0')
plt.plot(fr[0,:],np.abs(vplist01[5,:]),'g', label= '$\lambda_l$=0.1')
plt.plot(fr[0,:],np.abs(vplist02[5,:]),'b', label= '$\lambda_l$=0.2')
plt.plot(fr[0,:],np.abs(vplist03[5,:]),'k', label= '$\lambda_l$=0.3')
plt.plot(fr[0,:],np.abs(vplist04[5,:]),'c', label= '$\lambda_l$=0.4')
plt.plot(fr[0,:],np.abs(vplist05[5,:]),'r.--', label= '$\lambda_l$=0.5')
plt.plot(fr[0,:],np.abs(vplist06[5,:]),'g.--', label= '$\lambda_l$=0.6')
plt.plot(fr[0,:],np.abs(vplist07[5,:]),'b.--', label= '$\lambda_l$=0.7')
plt.plot(fr[0,:],np.abs(vplist08[5,:]),'k.--', label= '$\lambda_l$=0.8')
plt.plot(fr[0,:],np.abs(vplist09[5,:]),'c.--', label= '$\lambda_l$=0.9')
plt.plot(fr[0,:],np.abs(vplist10[5,:]),'y', label= '$\lambda_l$=1.0')
plt.xlabel('Base excitation frequency $fr$')
plt.ylabel('Amplitude of the output voltage $V_p$')
plt.title('Amplitude of the output voltage $V_p$ versus base excitation frequency $fr$ when $R_l = 1000\ \Omega$')
plt.legend(loc='lower right')
# plt.xscale('log')
plt.yscale('log')
plt.xlim(1,100)

# plt.savefig('fig_output_voltage_vs_frequency_laml.jpg',dpi=300)
# plt.savefig('fig_output_voltage_vs_frequency_laml.eps')
# plt.savefig('fig_output_voltage_vs_frequency_laml.pdf')



## plot 2



fig = plt.figure(1)
ax  = fig.gca(projection='3d')
# surf01 = ax.plot_surface(np.log10(fr), np.log10(Rl), np.log10(np.abs(vplist01)), cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# surf02 = ax.plot_surface(np.log10(fr), np.log10(Rl), np.log10(np.abs(vplist02)), cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# surf03 = ax.plot_surface(np.log10(fr), np.log10(Rl), np.log10(np.abs(vplist03)), cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# surf04 = ax.plot_surface(np.log10(fr), np.log10(Rl), np.log10(np.abs(vplist04)), cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# surf05 = ax.plot_surface(np.log10(fr), np.log10(Rl), np.log10(np.abs(vplist05)), cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# fr = np.log10(fr)
# Rl = np.log10(Rl)


surf01 = ax.plot_surface(fr, Rl, np.abs(vplist01), cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
# surf02 = ax.plot_surface(fr, Rl, np.abs(vplist02), cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# surf03 = ax.plot_surface(fr, Rl, np.abs(vplist03), cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# surf04 = ax.plot_surface(fr, Rl, np.abs(vplist04), cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# surf05 = ax.plot_surface(fr, Rl, np.abs(vplist05), cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# ax.set_zlim(-10.0, 10.0)
# ax.xaxis.set_scale('log')
# ax.yaxis.set_scale('log')
ax.zaxis.set_scale('log')
# ax.set_zscale('log')
# ax.set_xscale('log')
# print(dir(ax.xaxis))
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# fig.colorbar(surf, shrink=0.5, aspect=5)


# xticks = [1e0,1e1,1e2,1e3]
# yticks = [1e0,1e1,1e2,1e3,1e4,1e5,1e6,1e7]
# zticks = np.logspace(-5,5,11)
# ax.set_xticks(np.log10(xticks))
# ax.set_xticklabels(xticks)
# ax.set_yticks(np.log10(yticks))
# ax.set_yticklabels(yticks)
# ax.set_zticks(np.log10(zticks))
# ax.set_zticklabels(zticks)


plt.show()



# ['OFFSETTEXTPAD', '_AXINFO', '_PLANES', '__class__', '__delattr__', '__dict__', 
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
# '__getstate__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', 
# '__module__', '__name__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
# '__weakref__', '_agg_filter', '_alpha', '_animated', '_autolabelpos', 
# '_axes', '_axinfo', '_clipon', '_clippath', '_contains', '_copy_tick_props', 
# '_get_coord_info', '_get_label', '_get_offset_text', 
# '_get_pixel_distance_along_axis', '_get_tick', '_get_tick_bboxes', 
# '_gid', '_gridOnMajor', '_gridOnMinor', '_label', '_lastNumMajorTicks', 
# '_lastNumMinorTicks', '_major_tick_kw', '_minor_tick_kw', '_mouseover', 
# '_oid', '_path_effects', '_picker', '_propobservers', '_rasterized', 
# '_remove_method', '_rotate_label', '_scale', '_set_artist_props', 
# '_set_gc_clip', '_set_scale', '_sketch', '_smart_bounds', '_snap', 
# '_stale', '_transform', '_transformSet', '_translate_tick_kw', '_update_axisinfo', 
# '_update_label_position', '_update_offset_text_position', '_update_offset_text_postion', 
# '_update_ticks', '_url', '_visible', 'add_callback', 'adir', 'aname', 'axes', 'axis_date', 
# 'axis_name', 'callbacks', 'cla', 'clipbox', 'contains', 'convert_units', 'convert_xunits', 
# 'convert_yunits', 'converter', 'd_interval', 'draw', 'draw_pane', 'eventson', 'figure', 
# 'findobj', 'format_cursor_data', 'get_agg_filter', 'get_alpha', 'get_animated', 'get_axes', 
# 'get_children', 'get_clip_box', 'get_clip_on', 'get_clip_path', 'get_contains', 'get_cursor_data', 
# 'get_data_interval', 'get_figure', 'get_gid', 'get_gridlines', 'get_label', 'get_label_position', 
# 'get_label_text', 'get_major_formatter', 'get_major_locator', 'get_major_ticks', 'get_majorticklabels', 
# 'get_majorticklines', 'get_majorticklocs', 'get_minor_formatter', 'get_minor_locator', 'get_minor_ticks', 
# 'get_minorticklabels', 'get_minorticklines', 'get_minorticklocs', 'get_minpos', 'get_offset_text', 
# 'get_path_effects', 'get_picker', 'get_pickradius', 'get_rasterized', 'get_rotate_label', 'get_scale', 
# 'get_sketch_params', 'get_smart_bounds', 'get_snap', 'get_text_heights', 'get_tick_positions', 
# 'get_ticklabel_extents', 'get_ticklabels', 'get_ticklines', 'get_ticklocs', 'get_ticks_position', 
# 'get_tightbbox', 'get_transform', 'get_transformed_clip_path_and_affine', 'get_units', 'get_url', 
# 'get_view_interval', 'get_visible', 'get_window_extent', 'get_zorder', 'grid', 'gridlines', 
# 'have_units', 'hitlist', 'init3d', 'isDefault_label', 'isDefault_majfmt', 'isDefault_majloc', 
# 'isDefault_minfmt', 'isDefault_minloc', 'is_figure_set', 'is_transform_set', 'iter_ticks', 
# 'label', 'label_position', 'labelpad', 'limit_range_for_scale', 'line', 'major', 'majorTicks', 
# 'minor', 'minorTicks', 'mouseover', 'offsetText', 'offset_text_position', 'pan', 'pane', 
# 'pchanged', 'pick', 'pickable', 'pickradius', 'properties', 'remove', 'remove_callback', 
# 'reset_ticks', 'set', 'set_agg_filter', 'set_alpha', 'set_animated', 'set_axes', 
# 'set_clip_box', 'set_clip_on', 'set_clip_path', 'set_contains', 'set_data_interval', 
# 'set_default_intervals', 'set_figure', 'set_gid', 'set_label', 'set_label_coords', 
# 'set_label_position', 'set_label_text', 'set_major_formatter', 'set_major_locator', 
# 'set_minor_formatter', 'set_minor_locator', 'set_pane_color', 'set_pane_pos', 
# 'set_path_effects', 'set_picker', 'set_pickradius', 'set_rasterized', 'set_rotate_label', 
# 'set_sketch_params', 'set_smart_bounds', 'set_snap', 'set_tick_params', 'set_ticklabels', 
# 'set_ticks', 'set_ticks_position', 'set_transform', 'set_units', 'set_url', 'set_view_interval', 
# 'set_visible', 'set_zorder', 'stale', 'stale_callback', 'tick_bottom', 'tick_top', 'units', 
# 'update', 'update_from', 'update_units', 'v_interval', 'zoom', 'zorder']
# [Finished in 4.5s]