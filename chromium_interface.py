import subprocess as subsystem

from utils import find_path


class Interface:
    def __init__(self):
        self.commandline = []
        self.options = {"cmdline_args": self.commandline, "app_mode": True}

    def with_accept_empty_variations_seed_signature(self):
        self.commandline.extend(["--accept-empty-variations-seed-signature"])

    def with_accept_lang(self, lang):
        self.commandline.extend(["--accept-lang=" + lang])

    def with_accept_resource_provider(self, resource_provider):
        self.commandline.extend(["--accept-resource-provider=" + resource_provider])

    def with_adaboost(self):
        self.commandline.extend(["--adaboost"])

    def with_add_gpu_appcontainer_caps(self, value):
        self.commandline.extend(["--add-gpu-appcontainer-caps=" + value])

    def with_add_xr_appcontainer_caps(self, value):
        self.commandline.extend(["--add-xr-appcontainer-caps=" + value])

    def with_additional_private_state_token_key_commitments(self, commitments):
        self.commandline.extend(
            ["--additional-private-state-token-key-commitments=" + commitments]
        )

    def with_aggressive_cache_discard(self):
        self.commandline.extend(["--aggressive-cache-discard"])

    def with_all(self):
        self.commandline.extend(["--all"])

    def with_all_renderers(self):
        self.commandline.extend(["--all-renderers"])

    def with_allarticles(self):
        self.commandline.extend(["--allarticles"])

    def with_allow_command_line_plugins(self):
        self.commandline.extend(["--allow-command-line-plugins"])

    def with_allow_cross_origin_auth_prompt(self):
        self.commandline.extend(["--allow-cross-origin-auth-prompt"])

    def with_allow_empty_passwords_in_tests(self):
        self.commandline.extend(["--allow-empty-passwords-in-tests"])

    def with_allow_external_pages(self):
        self.commandline.extend(["--allow-external-pages"])

    def with_allow_failed_policy_fetch_for_test(self):
        self.commandline.extend(["--allow-failed-policy-fetch-for-test"])

    def with_allow_file_access_from_files(self):
        self.commandline.extend(["--allow-file-access-from-files"])

    def with_allow_future_manifest_version(self):
        self.commandline.extend(["--allow-future-manifest-version"])

    def with_allow_http_background_page(self):
        self.commandline.extend(["--allow-http-background-page"])

    def with_allow_http_screen_capture(self):
        self.commandline.extend(["--allow-http-screen-capture"])

    def with_allow_insecure_localhost(self):
        self.commandline.extend(["--allow-insecure-localhost"])

    def with_allow_legacy_extension_manifests(self):
        self.commandline.extend(["--allow-legacy-extension-manifests"])

    def with_allow_loopback_in_peer_connection(self):
        self.commandline.extend(["--allow-loopback-in-peer-connection"])

    def with_allow_nacl_crxfs_api(self, value):
        self.commandline.extend(["--allow-nacl-crxfs-api=" + value])

    def with_allow_nacl_file_handle_api(self, value):
        self.commandline.extend(["--allow-nacl-file-handle-api=" + value])

    def with_allow_nacl_socket_api(self, value):
        self.commandline.extend(["--allow-nacl-socket-api=" + value])

    def with_allow_os_install(self):
        self.commandline.extend(["--allow-os-install"])

    def with_allow_pre_commit_input(self):
        self.commandline.extend(["--allow-pre-commit-input"])

    def with_allow_profiles_outside_user_dir(self):
        self.commandline.extend(["--allow-profiles-outside-user-dir"])

    def with_allow_ra_in_dev_mode(self, value):
        self.commandline.extend(["--allow-ra-in-dev-mode=" + value])

    def with_allow_running_insecure_content(self, value):
        self.commandline.extend(["--allow-running-insecure-content=" + value])

    def with_allow_sandbox_debugging(self):
        self.commandline.extend(["--allow-sandbox-debugging"])

    def with_allow_silent_push(self):
        self.commandline.extend(["--allow-silent-push"])

    def with_allow_third_party_modules(self, value):
        self.commandline.extend(["--allow-third-party-modules=" + value])

    def with_allowlisted_extension_id(self, extension_id):
        self.commandline.extend(["--allow-listed-extension-id=" + extension_id])

    def with_almanac_api_url(self, url):
        self.commandline.extend(["--almanac-api-url=" + url])

    def with_alsa_amp_device_name(self, device_name):
        self.commandline.extend(["--alsa-amp-device-name=" + device_name])

    def with_alsa_amp_element_name(self, element_name):
        self.commandline.extend(["--alsa-amp-element-name=" + element_name])

    def with_alsa_check_close_timeout(self, timeout):
        self.commandline.extend(["--alsa-check-close-timeout=" + str(timeout)])

    def with_alsa_enable_upsampling(self, enable):
        self.commandline.extend(["--alsa-enable-upsampling=" + str(enable)])

    def with_alsa_fixed_output_sample_rate(self, sample_rate):
        self.commandline.extend(["--alsa-fixed-output-sample-rate=" + str(sample_rate)])

    def with_alsa_input_device(self, device):
        self.commandline.extend(["--alsa-input-device=" + device])

    def with_alsa_mute_device_name(self, device_name):
        self.commandline.extend(["--alsa-mute-device-name=" + device_name])

    def with_alsa_mute_element_name(self, element_name):
        self.commandline.extend(["--alsa-mute-element-name=" + element_name])

    def with_alsa_output_avail_min(self, avail_min):
        self.commandline.extend(["--alsa-output-avail-min=" + str(avail_min)])

    def with_alsa_output_buffer_size(self, buffer_size):
        self.commandline.extend(["--alsa-output-buffer-size=" + str(buffer_size)])

    def with_alsa_output_device(self, device):
        self.commandline.extend(["--alsa-output-device=" + device])

    def with_alsa_output_period_size(self, period_size):
        self.commandline.extend(["--alsa-output-period-size=" + str(period_size)])

    def with_alsa_output_start_threshold(self, start_threshold):
        self.commandline.extend(
            ["--alsa-output-start-threshold=" + str(start_threshold)]
        )

    def with_alsa_volume_device_name(self, device_name):
        self.commandline.extend(["--alsa-volume-device-name=" + device_name])

    def with_alsa_volume_element_name(self, element_name):
        self.commandline.extend(["--alsa-volume-element-name=" + element_name])

    def with_also_emit_success_logs(self, enable):
        self.commandline.extend(["--also-emit-success-logs=" + str(enable)])

    def with_always_enable_hdcp(self, enable):
        self.commandline.extend(["--always-enable-hdcp=" + str(enable)])

    def with_always_use_complex_text(self, enable):
        self.commandline.extend(["--always-use-complex-text=" + str(enable)])

    def with_angle(self, value):
        self.commandline.extend(["--angle=" + str(value)])

    def with_animated_image_resume(self, enable):
        self.commandline.extend(["--animated-image-resume=" + str(enable)])

    def with_animation_duration_scale(self, scale):
        self.commandline.extend(["--animation-duration-scale=" + str(scale)])

    def with_app(self, url):
        self.commandline.extend(["--app=%s" % url])

    def with_app_auto_launched(self):
        self.commandline.extend(["--app-auto-launched"])

    def with_app_id(self, app_id):
        self.commandline.extend(["--app-id=" + app_id])

    def with_app_launch_url_for_shortcuts_menu_item(self, url):
        self.commandline.extend(["--app-launch-url-for-shortcuts-menu-item=" + url])

    def with_app_mode_auth_code(self, auth_code):
        self.commandline.extend(["--app-mode-auth-code=" + auth_code])

    def with_app_mode_oauth_token(self, oauth_token):
        self.commandline.extend(["--app-mode-oauth-token=" + oauth_token])

    def with_app_mode_oem_manifest(self, manifest):
        self.commandline.extend(["--app-mode-oem-manifest=" + manifest])

    def with_app_run_on_os_login_mode(self, mode):
        self.commandline.extend(["--app-run-on-os-login-mode=" + mode])

    def with_app_shell_allow_roaming(self):
        self.commandline.extend(["--app-shell-allow-roaming"])

    def with_app_shell_host_window_size(self, size):
        self.commandline.extend(["--app-shell-host-window-size=" + size])

    def with_app_shell_preferred_network(self, network):
        self.commandline.extend(["--app-shell-preferred-network=" + network])

    def with_apps_gallery_download_url(self, url):
        self.commandline.extend(["--apps-gallery-download-url=" + url])

    def with_apps_gallery_update_url(self, url):
        self.commandline.extend(["--apps-gallery-update-url=" + url])

    def with_apps_gallery_url(self, url):
        self.commandline.extend(["--apps-gallery-url=" + url])

    def with_apps_keep_chrome_alive_in_tests(self):
        self.commandline.extend(["--apps-keep-chrome-alive-in-tests"])

    def with_arc_availability(self):
        self.commandline.extend(["--arc-availability"])

    def with_arc_available(self):
        self.commandline.extend(["--arc-available"])

    def with_arc_block_keymint(self):
        self.commandline.extend(["--arc-block-keymint"])

    def with_arc_data_cleanup_on_start(self):
        self.commandline.extend(["--arc-data-cleanup-on-start"])

    def with_arc_disable_app_sync(self):
        self.commandline.extend(["--arc-disable-app-sync"])

    def with_arc_disable_dexopt_cache(self):
        self.commandline.extend(["--arc-disable-dexopt-cache"])

    def with_arc_disable_download_provider(self):
        self.commandline.extend(["--arc-disable-download-provider"])

    def with_arc_disable_gms_core_cache(self):
        self.commandline.extend(["--arc-disable-gms-core-cache"])

    def with_arc_disable_locale_sync(self):
        self.commandline.extend(["--arc-disable-locale-sync"])

    def with_arc_disable_media_store_maintenance(self):
        self.commandline.extend(["--arc-disable-media-store-maintenance"])

    def with_arc_disable_play_auto_install(self):
        self.commandline.extend(["--arc-disable-play-auto-install"])

    def with_arc_disable_tts_cache(self):
        self.commandline.extend(["--arc-disable-tts-cache"])

    def with_arc_erofs(self):
        self.commandline.extend(["--arc-erofs"])

    def with_arc_force_mount_android_volumes_in_files(self):
        self.commandline.extend(["--arc-force-mount-android-volumes-in-files"])

    def with_arc_force_show_optin_ui(self):
        self.commandline.extend(["--arc-force-show-optin-ui"])

    def with_arc_generate_play_auto_install(self):
        self.commandline.extend(["--arc-generate-play-auto-install"])

    def with_arc_host_ureadahead_mode(self):
        self.commandline.extend(["--arc-host-ureadahead-mode"])

    def with_arc_install_event_chrome_log_for_tests(self):
        self.commandline.extend(["--arc-install-event-chrome-log-for-tests"])

    def with_arc_packages_cache_mode(self):
        self.commandline.extend(["--arc-packages-cache-mode"])

    def with_arc_play_store_auto_update(self):
        self.commandline.extend(["--arc-play-store-auto-update"])

    def with_arc_scale(self):
        self.commandline.extend(["--arc-scale"])

    def with_arc_start_mode(self):
        self.commandline.extend(["--arc-start-mode"])

    def with_arc_tos_host_for_tests(self):
        self.commandline.extend(["--arc-tos-host-for-tests"])

    def with_arc_use_dev_caches(self):
        self.commandline.extend(["--arc-use-dev-caches"])

    def with_arcore(self):
        self.commandline.extend(["--arcore"])

    def with_arcvm_ureadahead_mode(self):
        self.commandline.extend(["--arcvm-ureadahead-mode"])

    def with_arcvm_use_hugepages(self):
        self.commandline.extend(["--arcvm-use-hugepages"])

    def with_as_browser(self):
        self.commandline.extend(["--as-browser"])

    def with_ash_allow_default_shelf_pin_layout_ignoring_sync(self):
        self.commandline.extend(["--ash-allow-default-shelf-pin-layout-ignoring-sync"])

    def with_ash_bypass_glanceables_pref(self):
        self.commandline.extend(["--ash-bypass-glanceables-pref"])

    def with_ash_clear_fast_ink_buffer(self):
        self.commandline.extend(["--ash-clear-fast-ink-buffer"])

    def with_ash_constrain_pointer_to_root(self):
        self.commandline.extend(["--ash-constrain-pointer-to-root"])

    def with_ash_contextual_nudges_interval(self):
        self.commandline.extend(["--ash-contextual-nudges-interval"])

    def with_ash_contextual_nudges_reset_shown_count(self):
        self.commandline.extend(["--ash-contextual-nudges-reset-shown-count"])

    def with_ash_debug_shortcuts(self):
        self.commandline.extend(["--ash-debug-shortcuts"])

    def with_ash_dev_shortcuts(self):
        self.commandline.extend(["--ash-dev-shortcuts"])

    def with_ash_disable_touch_exploration_mode(self):
        self.commandline.extend(["--ash-disable-touch-exploration-mode"])

    def with_ash_enable_magnifier_key_scroller(self):
        self.commandline.extend(["--ash-enable-magnifier-key-scroller"])

    def with_ash_enable_palette_on_all_displays(self):
        self.commandline.extend(["--ash-enable-palette-on-all-displays"])

    def with_ash_enable_software_mirroring(self):
        self.commandline.extend(["--ash-enable-software-mirroring"])

    def with_ash_enable_unified_desktop(self):
        self.commandline.extend(["--ash-enable-unified-desktop"])

    def with_ash_hide_notifications_for_factory(self):
        self.commandline.extend(["--ash-hide-notifications-for-factory"])

    def with_ash_host_window_bounds(self):
        self.commandline.extend(["--ash-host-window-bounds"])

    def with_ash_no_nudges(self):
        self.commandline.extend(["--ash-no-nudges"])

    def with_ash_power_button_position(self):
        self.commandline.extend(["--ash-power-button-position"])

    def with_ash_side_volume_button_position(self):
        self.commandline.extend(["--ash-side-volume-button-position"])

    def with_ash_touch_hud(self):
        self.commandline.extend(["--ash-touch-hud"])

    def with_attestation_server(self):
        self.commandline.extend(["--attestation-server"])

    def with_attribution_reporting_debug_mode(self):
        self.commandline.extend(["--attribution-reporting-debug-mode"])

    def with_audio(self):
        self.commandline.extend(["--audio"])

    def with_audio_buffer_size(self, size):
        self.commandline.extend(["--audio-buffer-size=" + size])

    def with_audio_capturer_with_echo_cancellation(self):
        self.commandline.extend(["--audio-capturer-with-echo-cancellation"])

    def with_audio_codecs_from_edid(self):
        self.commandline.extend(["--audio-codecs-from-edid"])

    def with_audio_output_channels(self, channels):
        self.commandline.extend(["--audio-output-channels=" + channels])

    def with_audio_output_sample_rate(self, rate):
        self.commandline.extend(["--audio-output-sample-rate=" + rate])

    def with_audio_process_high_priority(self):
        self.commandline.extend(["--audio-process-high-priority"])

    def with_aue_reached_for_update_required_test(self):
        self.commandline.extend(["--aue-reached-for-update-required-test"])

    def with_aura_legacy_power_button(self):
        self.commandline.extend(["--aura-legacy-power-button"])

    def with_auth_server_allowlist(self):
        self.commandline.extend(["--auth-server-allowlist"])

    def with_auth_spnego_account_type(self):
        self.commandline.extend(["--auth-spnego-account-type"])

    def with_auto(self):
        self.commandline.extend(["--auto"])

    def with_auto_accept_camera_and_microphone_capture(self):
        self.commandline.extend(["--auto-accept-camera-and-microphone-capture"])

    def with_auto_accept_this_tab_capture(self):
        self.commandline.extend(["--auto-accept-this-tab-capture"])

    def with_auto_grant_captured_surface_control_prompt(self):
        self.commandline.extend(["--auto-grant-captured-surface-control-prompt"])

    def with_auto_open_devtools_for_tabs(self):
        self.commandline.extend(["--auto-open-devtools-for-tabs"])

    def with_auto_reject_this_tab_capture(self):
        self.commandline.extend(["--auto-reject-this-tab-capture"])

    def with_auto_select_desktop_capture_source(self):
        self.commandline.extend(["--auto-select-desktop-capture-source"])

    def with_auto_select_tab_capture_source_by_title(self):
        self.commandline.extend(["--auto-select-tab-capture-source-by-title"])

    def with_auto_select_window_capture_source_by_title(self):
        self.commandline.extend(["--auto-select-window-capture-source-by-title"])

    def with_autofill_api_key(self):
        self.commandline.extend(["--autofill-api-key"])

    def with_autofill_server_url(self):
        self.commandline.extend(["--autofill-server-url"])

    def with_autofill_upload_throttling_period_in_days(self):
        self.commandline.extend(["--autofill-upload-throttling-period-in-days"])

    def with_autoplay_policy(self, policy):
        self.commandline.extend(["--autoplay-policy=" + policy])

    def with_back_gesture_horizontal_threshold(self, threshold):
        self.commandline.extend(["--back-gesture-horizontal-threshold=" + threshold])

    def with_background_tracing_output_file(self, file):
        self.commandline.extend(["--background-tracing-output-file=" + file])

    def with_bgra(self):
        self.commandline.extend(["--bgra"])

    def with_biod_fake(self):
        self.commandline.extend(["--biod-fake"])

    def with_blink_settings(self, settings):
        self.commandline.extend(["--blink-settings=" + settings])

    def with_block_new_web_contents(self):
        self.commandline.extend(["--block-new-web-contents"])

    def with_bootstrap(self):
        self.commandline.extend(["--bootstrap"])

    def with_borealis_launch_options(self, options):
        self.commandline.extend(["--borealis-launch-options=" + options])

    def with_bottom_gesture_start_height(self, height):
        self.commandline.extend(["--bottom-gesture-start-height=" + height])

    def with_bound_session_cookie_rotation_delay(self, delay):
        self.commandline.extend(["--bound-session-cookie-rotation-delay=" + delay])

    def with_bound_session_cookie_rotation_result(self, result):
        self.commandline.extend(["--bound-session-cookie-rotation-result=" + result])

    def with_browser(self, browser_path):
        self.commandline.extend(["--browser=" + browser_path])

    def with_browser_data_backward_migration_for_user(
        self,
    ):
        self.commandline.extend(["--browser-data-backward-migration-for-user"])

    def with_browser_data_backward_migration_mode(self, mode):
        self.commandline.extend(["--browser-data-backward-migration-mode=" + mode])

    def with_browser_data_migration_for_user(
        self,
    ):
        self.commandline.extend(["--browser-data-migration-for-user"])

    def with_browser_data_migration_mode(self, mode):
        self.commandline.extend(["--browser-data-migration-mode=" + mode])

    def with_browser_startup_dialog(
        self,
    ):
        self.commandline.extend(["--browser-startup-dialog"])

    def with_browser_subprocess_path(self, path):
        self.commandline.extend(["--browser-subprocess-path=" + path])

    def with_browser_test(
        self,
    ):
        self.commandline.extend(["--browser-test"])

    def with_browser_ui_tests_verify_pixels(
        self,
    ):
        self.commandline.extend(["--browser-ui-tests-verify-pixels"])

    def with_bwsi(
        self,
    ):
        self.commandline.extend(["--bwsi"])

    def with_bypass_app_banner_engagement_checks(
        self,
    ):
        self.commandline.extend(["--bypass-app-banner-engagement-checks"])

    def with_bypass_installable_message_throttle_for_testing(
        self,
    ):
        self.commandline.extend(["--bypass-installable-message-throttle-for-testing"])

    def with_campbell_key(self, key):
        self.commandline.extend(["--campbell-key=" + key])

    def with_canvas_2d_layers(
        self,
    ):
        self.commandline.extend(["--canvas-2d-layers"])

    def with_cardboard(
        self,
    ):
        self.commandline.extend(["--cardboard"])

    def with_cast_app_background_color(self, color):
        self.commandline.extend(["--cast-app-background-color=" + color])

    def with_cast_developer_certificate_path(self, path):
        self.commandline.extend(["--cast-developer-certificate-path=" + path])

    def with_cast_initial_screen_height(self, height):
        self.commandline.extend(["--cast-initial-screen-height=" + height])

    def with_cast_initial_screen_width(self, width):
        self.commandline.extend(["--cast-initial-screen-width=" + width])

    def with_cast_log_device_cert_chain(
        self,
    ):
        self.commandline.extend(["--cast-log-device-cert-chain"])

    def with_cast_mirroring_target_playout_delay(self, delay):
        self.commandline.extend(["--cast-mirroring-target-playout-delay=" + delay])

    def with_cast_mojo_broker_path(self, path):
        self.commandline.extend(["--cast-mojo-broker-path=" + path])

    def with_cast_streaming_force_disable_hardware_h264(
        self,
    ):
        self.commandline.extend(["--cast-streaming-force-disable-hardware-h264"])

    def with_cast_streaming_force_disable_hardware_vp8(
        self,
    ):
        self.commandline.extend(["--cast-streaming-force-disable-hardware-vp8"])

    def with_cast_streaming_force_enable_hardware_h264(
        self,
    ):
        self.commandline.extend(["--cast-streaming-force-enable-hardware-h264"])

    def with_cast_streaming_force_enable_hardware_vp8(
        self,
    ):
        self.commandline.extend(["--cast-streaming-force-enable-hardware-vp8"])

    def with_cc_layer_tree_test_long_timeout(
        self,
    ):
        self.commandline.extend(["--cc-layer-tree-test-long-timeout"])

    def with_cc_layer_tree_test_no_timeout(
        self,
    ):
        self.commandline.extend(["--cc-layer-tree-test-no-timeout"])

    def with_cc_scroll_animation_duration_in_seconds(self, duration):
        self.commandline.extend(
            ["--cc-scroll-animation-duration-in-seconds=" + duration]
        )

    def with_cdm(self, cdm_path):
        self.commandline.extend(["--cdm=" + cdm_path])

    def with_cdm_data_directory(self, directory):
        self.commandline.extend(["--cdm-data-directory=" + directory])

    def with_cdm_data_quota_bytes(self, quota):
        self.commandline.extend(["--cdm-data-quota-bytes=" + quota])

    def with_cellular_first(
        self,
    ):
        self.commandline.extend(["--cellular-first"])

    def with_change_stack_guard_on_fork(
        self,
    ):
        self.commandline.extend(["--change-stack-guard-on-fork"])

    def with_character(self, character_value):
        self.commandline.extend(["--character=" + character_value])

    def with_check_accessibility_permission(
        self,
    ):
        self.commandline.extend(["--check-accessibility-permission"])

    def with_check_damage_early(
        self,
    ):
        self.commandline.extend(["--check-damage-early"])

    def with_check_for_update_interval(self, interval):
        self.commandline.extend(["--check-for-update-interval=" + interval])

    def with_check_permission(
        self,
    ):
        self.commandline.extend(["--check-permission"])

    def with_check_screen_recording_permission(
        self,
    ):
        self.commandline.extend(["--check-screen-recording-permission"])

    def with_child_wallpaper_large(self, wallpaper_path):
        self.commandline.extend(["--child-wallpaper-large=" + wallpaper_path])

    def with_child_wallpaper_small(self, wallpaper_path):
        self.commandline.extend(["--child-wallpaper-small=" + wallpaper_path])

    def with_cipher_suite_blacklist(self, suites):
        self.commandline.extend(["--cipher-suite-blacklist=" + suites])

    def with_clamshell(
        self,
    ):
        self.commandline.extend(["--clamshell"])

    def with_clear_key_cdm_path_for_testing(
        self,
    ):
        self.commandline.extend(["--clear-key-cdm-path-for-testing"])

    def with_clear_token_service(
        self,
    ):
        self.commandline.extend(["--clear-token-service"])

    def with_compensate_for_unstable_pinch_zoom(
        self,
    ):
        self.commandline.extend(["--compensate-for-unstable-pinch-zoom"])

    def with_compile_shader_always_succeeds(
        self,
    ):
        self.commandline.extend(["--compile-shader-always-succeeds"])

    def with_component_updater(
        self,
    ):
        self.commandline.extend(["--component-updater"])

    def with_component_updater_trust_tokens_component_path(self, path):
        self.commandline.extend(
            ["--component-updater-trust-tokens-component-path=" + path]
        )

    def with_conditional_focus_window_ms(self, milliseconds):
        self.commandline.extend(["--conditional-focus-window-ms=" + milliseconds])

    def with_connectivity_check_url(self, url):
        self.commandline.extend(["--connectivity-check-url=" + url])

    def with_conservative(
        self,
    ):
        self.commandline.extend(["--conservative"])

    def with_container_app_preinstall_key(self, key):
        self.commandline.extend(["--container-app-preinstall-key=" + key])

    def with_content_shell_devtools_tab_target(
        self,
    ):
        self.commandline.extend(["--content-shell-devtools-tab-target"])

    def with_content_shell_hide_toolbar(
        self,
    ):
        self.commandline.extend(["--content-shell-hide-toolbar"])

    def with_content_shell_host_window_size(self, size):
        self.commandline.extend(["--content-shell-host-window-size=" + size])

    def with_context_provider(self, provider):
        self.commandline.extend(["--context-provider=" + provider])

    def with_controller(
        self,
    ):
        self.commandline.extend(["--controller"])

    def with_coral_feature_key(self, key):
        self.commandline.extend(["--coral-feature-key=" + key])

    def with_cors_exempt_headers(self, headers):
        self.commandline.extend(["--cors-exempt-headers=" + headers])

    def with_crash_dumps_dir(self, directory):
        self.commandline.extend(["--crash-dumps-dir=" + directory])

    def with_crash_loop_before(self, loop_time):
        self.commandline.extend(["--crash-loop-before=" + loop_time])

    def with_crash_on_failure(
        self,
    ):
        self.commandline.extend(["--crash-on-failure"])

    def with_crash_on_hang_threads(
        self,
    ):
        self.commandline.extend(["--crash-on-hang-threads"])

    def with_crash_server_url(self, url):
        self.commandline.extend(["--crash-server-url=" + url])

    def with_crash_test(
        self,
    ):
        self.commandline.extend(["--crash-test"])

    def with_crashpad_handler(self, handler_path):
        self.commandline.extend(["--crashpad-handler=" + handler_path])

    def with_crashpad_handler_pid(self, pid):
        self.commandline.extend(["--crashpad-handler-pid=" + str(pid)])

    def with_create_browser_on_startup_for_tests(
        self,
    ):
        self.commandline.extend(["--create-browser-on-startup-for-tests"])

    def with_credits(
        self,
    ):
        self.commandline.extend(["--credits"])

    def with_cros_disks_fake(
        self,
    ):
        self.commandline.extend(["--cros-disks-fake"])

    def with_cros_postlogin_data_fd(self, fd):
        self.commandline.extend(["--cros-postlogin-data-fd=" + str(fd)])

    def with_cros_postlogin_log_file(self, log_file):
        self.commandline.extend(["--cros-postlogin-log-file=" + log_file])

    def with_cros_region(self, region):
        self.commandline.extend(["--cros-region=" + region])

    def with_cros_startup_data_fd(self, fd):
        self.commandline.extend(["--cros-startup-data-fd=" + str(fd)])

    def with_crosh_command(self, command):
        self.commandline.extend(["--crosh-command=" + command])

    def with_cryptauth_http_host(self, host):
        self.commandline.extend(["--cryptauth-http-host=" + host])

    def with_cryptauth_v2_devicesync_http_host(self, host):
        self.commandline.extend(["--cryptauth-v2-devicesync-http-host=" + host])

    def with_cryptauth_v2_enrollment_http_host(self, host):
        self.commandline.extend(["--cryptauth-v2-enrollment-http-host=" + host])

    def with_cryptohome_ignore_cleanup_ownership_for_testing(self):
        self.commandline.extend(["--cryptohome-ignore-cleanup-ownership-for-testing"])

    def with_cryptohome_recovery_service_base_url(self, url):
        self.commandline.extend(["--cryptohome-recovery-service-base-url=" + url])

    def with_cryptohome_recovery_use_test_env(self):
        self.commandline.extend(["--cryptohome-recovery-use-test-env"])

    def with_cryptohome_use_authsession(
        self,
    ):
        self.commandline.extend(["--cryptohome-use-authsession"])

    def with_cryptohome_use_old_encryption_for_testing(
        self,
    ):
        self.commandline.extend(["--cryptohome-use-old-encryption-for-testing"])

    def with_custom_android_messages_domain(self, domain):
        self.commandline.extend(["--custom-android-messages-domain=" + domain])

    def with_custom_devtools_frontend(self, path):
        self.commandline.extend(["--custom-devtools-frontend=" + path])

    def with_custom_summary(self, summary):
        self.commandline.extend(["--custom-summary=" + summary])

    def with_d3d_support(
        self,
    ):
        self.commandline.extend(["--d3d-support"])

    def with_d3d11(
        self,
    ):
        self.commandline.extend(["--d3d11"])

    def with_d3d11_null(
        self,
    ):
        self.commandline.extend(["--d3d11-null"])

    def with_d3d11on12(
        self,
    ):
        self.commandline.extend(["--d3d11on12"])

    def with_d3d9(
        self,
    ):
        self.commandline.extend(["--d3d9"])

    def with_daemon(
        self,
    ):
        self.commandline.extend(["--daemon"])

    def with_dark_mode_settings(self, settings):
        self.commandline.extend(["--dark-mode-settings=" + settings])

    def with_data_path(self, path):
        self.commandline.extend(["--data-path=" + path])

    def with_data_quota_bytes(self, bytes):
        self.commandline.extend(["--data-quota-bytes=" + str(bytes)])

    def with_data_url_in_svg_use_enabled(
        self,
    ):
        self.commandline.extend(["--data-url-in-svg-use-enabled"])

    def with_dawn(
        self,
    ):
        self.commandline.extend(["--dawn"])

    def with_dawn_d3d11(
        self,
    ):
        self.commandline.extend(["--dawn-d3d11"])

    def with_dawn_d3d12(
        self,
    ):
        self.commandline.extend(["--dawn-d3d12"])

    def with_dawn_metal(
        self,
    ):
        self.commandline.extend(["--dawn-metal"])

    def with_dawn_swiftshader(
        self,
    ):
        self.commandline.extend(["--dawn-swiftshader"])

    def with_dawn_vulkan(
        self,
    ):
        self.commandline.extend(["--dawn-vulkan"])

    def with_dbus_stub(
        self,
    ):
        self.commandline.extend(["--dbus-stub"])

    def with_deadline_to_synchronize_surfaces(self, milliseconds):
        self.commandline.extend(
            ["--deadline-to-synchronize-surfaces=" + str(milliseconds)]
        )

    def with_debug_devtools(
        self,
    ):
        self.commandline.extend(["--debug-devtools"])

    def with_debug_packed_apps(
        self,
    ):
        self.commandline.extend(["--debug-packed-apps"])

    def with_debug_print(
        self,
    ):
        self.commandline.extend(["--debug-print"])

    def with_default_background_color(self, color):
        self.commandline.extend(["--default-background-color=" + color])

    def with_default_country_code(self, code):
        self.commandline.extend(["--default-country-code=" + code])

    def with_default_tile_height(self, height):
        self.commandline.extend(["--default-tile-height=" + str(height)])

    def with_default_tile_width(self, width):
        self.commandline.extend(["--default-tile-width=" + str(width)])

    def with_default_trace_buffer_size_limit_in_kb(self, limit):
        self.commandline.extend(
            ["--default-trace-buffer-size-limit-in-kb=" + str(limit)]
        )

    def with_default_wallpaper_is_oem(
        self,
    ):
        self.commandline.extend(["--default-wallpaper-is-oem"])

    def with_default_wallpaper_large(self, path):
        self.commandline.extend(["--default-wallpaper-large=" + path])

    def with_default_wallpaper_small(self, path):
        self.commandline.extend(["--default-wallpaper-small=" + path])

    def with_defer_external_display_timeout(self, milliseconds):
        self.commandline.extend(
            ["--defer-external-display-timeout=" + str(milliseconds)]
        )

    def with_defer_feature_list(
        self,
    ):
        self.commandline.extend(["--defer-feature-list"])

    def with_demo_mode_enrolling_username(self, username):
        self.commandline.extend(["--demo-mode-enrolling-username=" + username])

    def with_demo_mode_force_arc_offline_provision(
        self,
    ):
        self.commandline.extend(["--demo-mode-force-arc-offline-provision"])

    def with_demo_mode_highlights_extension(
        self,
    ):
        self.commandline.extend(["--demo-mode-highlights-extension"])

    def with_demo_mode_screensaver_extension(
        self,
    ):
        self.commandline.extend(["--demo-mode-screensaver-extension"])

    def with_demo_mode_swa_content_directory(self, directory):
        self.commandline.extend(["--demo-mode-swa-content-directory=" + directory])

    def with_deny_permission_prompts(
        self,
    ):
        self.commandline.extend(["--deny-permission-prompts"])

    def with_derelict_detection_timeout(self, milliseconds):
        self.commandline.extend(["--derelict-detection-timeout=" + str(milliseconds)])

    def with_derelict_idle_timeout(self, milliseconds):
        self.commandline.extend(["--derelict-idle-timeout=" + str(milliseconds)])

    def with_desktop_window_1080p(
        self,
    ):
        self.commandline.extend(["--desktop-window-1080p"])

    def with_deterministic_mode(
        self,
    ):
        self.commandline.extend(["--deterministic-mode"])

    def with_device_management_url(self, url):
        self.commandline.extend(["--device-management-url=" + url])

    def with_device_scale_factor(self, factor):
        self.commandline.extend(["--device-scale-factor=" + str(factor)])

    def with_devtools_code_coverage(
        self,
    ):
        self.commandline.extend(["--devtools-code-coverage"])

    def with_devtools_flags(self, flags):
        self.commandline.extend(["--devtools-flags=" + flags])

    def with_diagnostics(
        self,
    ):
        self.commandline.extend(["--diagnostics"])

    def with_diagnostics_format(self, format):
        self.commandline.extend(["--diagnostics-format=" + format])

    def with_diagnostics_recovery(
        self,
    ):
        self.commandline.extend(["--diagnostics-recovery"])

    def with_direct_composition_video_swap_chain_format(self, format):
        self.commandline.extend(
            ["--direct-composition-video-swap-chain-format=" + format]
        )

    def with_disable_2d_canvas_clip_aa(
        self,
    ):
        self.commandline.extend(["--disable-2d-canvas-clip-aa"])

    def with_disable_2d_canvas_image_chromium(
        self,
    ):
        self.commandline.extend(["--disable-2d-canvas-image-chromium"])

    def with_disable_3d_apis(
        self,
    ):
        self.commandline.extend(["--disable-3d-apis"])

    def with_disable_accelerated_2d_canvas(
        self,
    ):
        self.commandline.extend(["--disable-accelerated-2d-canvas"])

    def with_disable_accelerated_mjpeg_decode(
        self,
    ):
        self.commandline.extend(["--disable-accelerated-mjpeg-decode"])

    def with_disable_accelerated_video_decode(
        self,
    ):
        self.commandline.extend(["--disable-accelerated-video-decode"])

    def with_disable_accelerated_video_encode(
        self,
    ):
        self.commandline.extend(["--disable-accelerated-video-encode"])

    def with_disable_adpf(
        self,
    ):
        self.commandline.extend(["--disable-adpf"])

    def with_disable_angle_features(
        self,
    ):
        self.commandline.extend(["--disable-angle-features"])

    def with_disable_app_content_verification(
        self,
    ):
        self.commandline.extend(["--disable-app-content-verification"])

    def with_disable_arc_cpu_restriction(
        self,
    ):
        self.commandline.extend(["--disable-arc-cpu-restriction"])

    def with_disable_arc_data_wipe(
        self,
    ):
        self.commandline.extend(["--disable-arc-data-wipe"])

    def with_disable_arc_opt_in_verification(
        self,
    ):
        self.commandline.extend(["--disable-arc-opt-in-verification"])

    def with_disable_audio_input(
        self,
    ):
        self.commandline.extend(["--disable-audio-input"])

    def with_disable_auto_maximize_for_tests(
        self,
    ):
        self.commandline.extend(["--disable-auto-maximize-for-tests"])

    def with_disable_auto_reload(
        self,
    ):
        self.commandline.extend(["--disable-auto-reload"])

    def with_disable_auto_wpt_origin_isolation(
        self,
    ):
        self.commandline.extend(["--disable-auto-wpt-origin-isolation"])

    def with_disable_ax_menu_list(
        self,
    ):
        self.commandline.extend(["--disable-ax-menu-list"])

    def with_disable_back_forward_cache(
        self,
    ):
        self.commandline.extend(["--disable-back-forward-cache"])

    def with_disable_background_media_suspend(
        self,
    ):
        self.commandline.extend(["--disable-background-media-suspend"])

    def with_disable_background_networking(
        self,
    ):
        self.commandline.extend(["--disable-background-networking"])

    def with_disable_background_timer_throttling(
        self,
    ):
        self.commandline.extend(["--disable-background-timer-throttling"])

    def with_disable_backgrounding_occluded_windows(
        self,
    ):
        self.commandline.extend(["--disable-backgrounding-occluded-windows"])

    def with_disable_backing_store_limit(
        self,
    ):
        self.commandline.extend(["--disable-backing-store-limit"])

    def with_disable_best_effort_tasks(
        self,
    ):
        self.commandline.extend(["--disable-best-effort-tasks"])

    def with_disable_blink_features(self, features):
        self.commandline.extend(["--disable-blink-features=" + features])

    def with_disable_breakpad(
        self,
    ):
        self.commandline.extend(["--disable-breakpad"])

    def with_disable_cancel_all_touches(
        self,
    ):
        self.commandline.extend(["--disable-cancel-all-touches"])

    def with_disable_canvas_aa(
        self,
    ):
        self.commandline.extend(["--disable-canvas-aa"])

    def with_disable_checker_imaging(
        self,
    ):
        self.commandline.extend(["--disable-checker-imaging"])

    def with_disable_checking_optimization_guide_user_permissions(
        self,
    ):
        self.commandline.extend(
            ["--disable-checking-optimization-guide-user-permissions"]
        )

    def with_disable_chrome_tracing_computation(
        self,
    ):
        self.commandline.extend(["--disable-chrome-tracing-computation"])

    def with_disable_component_extensions_with_background_pages(
        self,
    ):
        self.commandline.extend(
            ["--disable-component-extensions-with-background-pages"]
        )

    def with_disable_component_update(
        self,
    ):
        self.commandline.extend(["--disable-component-update"])

    def with_disable_composited_antialiasing(
        self,
    ):
        self.commandline.extend(["--disable-composited-antialiasing"])

    def with_disable_cookie_encryption(
        self,
    ):
        self.commandline.extend(["--disable-cookie-encryption"])

    def with_disable_crash_reporter(
        self,
    ):
        self.commandline.extend(["--disable-crash-reporter"])

    def with_disable_databases(
        self,
    ):
        self.commandline.extend(["--disable-databases"])

    def with_disable_dawn_features(
        self,
    ):
        self.commandline.extend(["--disable-dawn-features"])

    def with_disable_default_apps(
        self,
    ):
        self.commandline.extend(["--disable-default-apps"])

    def with_disable_demo_mode(
        self,
    ):
        self.commandline.extend(["--disable-demo-mode"])

    def with_disable_dev_shm_usage(
        self,
    ):
        self.commandline.extend(["--disable-dev-shm-usage"])

    def with_disable_device_disabling(
        self,
    ):
        self.commandline.extend(["--disable-device-disabling"])

    def with_disable_dinosaur_easter_egg(
        self,
    ):
        self.commandline.extend(["--disable-dinosaur-easter-egg"])

    def with_disable_disallow_lacros(
        self,
    ):
        self.commandline.extend(["--disable-disallow-lacros"])

    def with_disable_domain_blocking_for_3d_apis(
        self,
    ):
        self.commandline.extend(["--disable-domain-blocking-for-3d-apis"])

    def with_disable_domain_reliability(
        self,
    ):
        self.commandline.extend(["--disable-domain-reliability"])

    def with_disable_drive_fs_for_testing(
        self,
    ):
        self.commandline.extend(["--disable-drive-fs-for-testing"])

    def with_disable_explicit_dma_fences(
        self,
    ):
        self.commandline.extend(["--disable-explicit-dma-fences"])

    def with_disable_extensions(
        self,
    ):
        self.commandline.extend(["--disable-extensions"])

    def with_disable_extensions_except(self, extensions):
        self.commandline.extend(["--disable-extensions-except=" + extensions])

    def with_disable_extensions_file_access_check(
        self,
    ):
        self.commandline.extend(["--disable-extensions-file-access-check"])

    def with_disable_extensions_http_throttling(
        self,
    ):
        self.commandline.extend(["--disable-extensions-http-throttling"])

    def with_disable_fetching_hints_at_navigation_start(
        self,
    ):
        self.commandline.extend(["--disable-fetching-hints-at-navigation-start"])

    def with_disable_field_trial_config(
        self,
    ):
        self.commandline.extend(["--disable-field-trial-config"])

    def with_disable_file_system(
        self,
    ):
        self.commandline.extend(["--disable-file-system"])

    def with_disable_fine_grained_time_zone_detection(
        self,
    ):
        self.commandline.extend(["--disable-fine-grained-time-zone-detection"])

    def with_disable_first_run_ui(
        self,
    ):
        self.commandline.extend(["--disable-first-run-ui"])

    def with_disable_font_subpixel_positioning(
        self,
    ):
        self.commandline.extend(["--disable-font-subpixel-positioning"])

    def with_disable_frame_rate_limit(
        self,
    ):
        self.commandline.extend(["--disable-frame-rate-limit"])

    def with_disable_gaia_services(
        self,
    ):
        self.commandline.extend(["--disable-gaia-services"])

    def with_disable_gesture_requirement_for_presentation(
        self,
    ):
        self.commandline.extend(["--disable-gesture-requirement-for-presentation"])

    def with_disable_gl_drawing_for_tests(
        self,
    ):
        self.commandline.extend(["--disable-gl-drawing-for-tests"])

    def with_disable_gl_error_limit(
        self,
    ):
        self.commandline.extend(["--disable-gl-error-limit"])

    def with_disable_gl_extensions(
        self,
    ):
        self.commandline.extend(["--disable-gl-extensions"])

    def with_disable_glsl_translator(
        self,
    ):
        self.commandline.extend(["--disable-glsl-translator"])

    def with_disable_gpu(
        self,
    ):
        self.commandline.extend(["--disable-gpu"])

    def with_disable_gpu_compositing(
        self,
    ):
        self.commandline.extend(["--disable-gpu-compositing"])

    def with_disable_gpu_driver_bug_workarounds(
        self,
    ):
        self.commandline.extend(["--disable-gpu-driver-bug-workarounds"])

    def with_disable_gpu_early_init(
        self,
    ):
        self.commandline.extend(["--disable-gpu-early-init"])

    def with_disable_gpu_memory_buffer_compositor_resources(
        self,
    ):
        self.commandline.extend(["--disable-gpu-memory-buffer-compositor-resources"])

    def with_disable_gpu_memory_buffer_video_frames(
        self,
    ):
        self.commandline.extend(["--disable-gpu-memory-buffer-video-frames"])

    def with_disable_gpu_process_crash_limit(
        self,
    ):
        self.commandline.extend(["--disable-gpu-process-crash-limit"])

    def with_disable_gpu_process_for_dx12_info_collection(
        self,
    ):
        self.commandline.extend(["--disable-gpu-process-for-dx12-info-collection"])

    def with_disable_gpu_program_cache(
        self,
    ):
        self.commandline.extend(["--disable-gpu-program-cache"])

    def with_disable_gpu_rasterization(
        self,
    ):
        self.commandline.extend(["--disable-gpu-rasterization"])

    def with_disable_gpu_sandbox(
        self,
    ):
        self.commandline.extend(["--disable-gpu-sandbox"])

    def with_disable_gpu_shader_disk_cache(
        self,
    ):
        self.commandline.extend(["--disable-gpu-shader-disk-cache"])

    def with_disable_gpu_vsync(
        self,
    ):
        self.commandline.extend(["--disable-gpu-vsync"])

    def with_disable_gpu_watchdog(
        self,
    ):
        self.commandline.extend(["--disable-gpu-watchdog"])

    def with_disable_hang_monitor(
        self,
    ):
        self.commandline.extend(["--disable-hang-monitor"])

    def with_disable_headless_mode(
        self,
    ):
        self.commandline.extend(["--disable-headless-mode"])

    def with_disable_hid_blocklist(
        self,
    ):
        self.commandline.extend(["--disable-hid-blocklist"])

    def with_disable_hid_detection_on_oobe(
        self,
    ):
        self.commandline.extend(["--disable-hid-detection-on-oobe"])

    def with_disable_highres_timer(
        self,
    ):
        self.commandline.extend(["--disable-highres-timer"])

    def with_disable_histogram_customizer(
        self,
    ):
        self.commandline.extend(["--disable-histogram-customizer"])

    def with_disable_image_animation_resync(
        self,
    ):
        self.commandline.extend(["--disable-image-animation-resync"])

    def with_disable_in_process_stack_traces(
        self,
    ):
        self.commandline.extend(["--disable-in-process-stack-traces"])

    def with_disable_input_event_activation_protection(
        self,
    ):
        self.commandline.extend(["--disable-input-event-activation-protection"])

    def with_disable_ios_password_suggestions(
        self,
    ):
        self.commandline.extend(["--disable-ios-password-suggestions"])

    def with_disable_ip_privacy_proxy(
        self,
    ):
        self.commandline.extend(["--disable-ip-privacy-proxy"])

    def with_disable_ipc_flooding_protection(
        self,
    ):
        self.commandline.extend(["--disable-ipc-flooding-protection"])

    def with_disable_javascript_harmony_shipping(
        self,
    ):
        self.commandline.extend(["--disable-javascript-harmony-shipping"])

    def with_disable_kill_after_bad_ipc(
        self,
    ):
        self.commandline.extend(["--disable-kill-after-bad-ipc"])

    def with_disable_lacros_keep_alive(
        self,
    ):
        self.commandline.extend(["--disable-lacros-keep-alive"])

    def with_disable_layer_tree_host_memory_pressure(
        self,
    ):
        self.commandline.extend(["--disable-layer-tree-host-memory-pressure"])

    def with_disable_lazy_loading(
        self,
    ):
        self.commandline.extend(["--disable-lazy-loading"])

    def with_disable_lcd_text(
        self,
    ):
        self.commandline.extend(["--disable-lcd-text"])

    def with_disable_legacy_window(
        self,
    ):
        self.commandline.extend(["--disable-legacy-window"])

    def with_disable_libassistant_logfile(
        self,
    ):
        self.commandline.extend(["--disable-libassistant-logfile"])

    def with_disable_local_storage(
        self,
    ):
        self.commandline.extend(["--disable-local-storage"])

    def with_disable_logging(
        self,
    ):
        self.commandline.extend(["--disable-logging"])

    def with_disable_logging_redirect(
        self,
    ):
        self.commandline.extend(["--disable-logging-redirect"])

    def with_disable_login_animations(
        self,
    ):
        self.commandline.extend(["--disable-login-animations"])

    def with_disable_login_lacros_opening(
        self,
    ):
        self.commandline.extend(["--disable-login-lacros-opening"])

    def with_disable_login_screen_apps(
        self,
    ):
        self.commandline.extend(["--disable-login-screen-apps"])

    def with_disable_low_end_device_mode(
        self,
    ):
        self.commandline.extend(["--disable-low-end-device-mode"])

    def with_disable_low_latency_dxva(
        self,
    ):
        self.commandline.extend(["--disable-low-latency-dxva"])

    def with_disable_low_res_tiling(
        self,
    ):
        self.commandline.extend(["--disable-low-res-tiling"])

    def with_disable_machine_cert_request(
        self,
    ):
        self.commandline.extend(["--disable-machine-cert-request"])

    def with_disable_main_frame_before_activation(
        self,
    ):
        self.commandline.extend(["--disable-main-frame-before-activation"])

    def with_disable_media_session_api(
        self,
    ):
        self.commandline.extend(["--disable-media-session-api"])

    def with_disable_metal_shader_cache(
        self,
    ):
        self.commandline.extend(["--disable-metal-shader-cache"])

    def with_disable_mipmap_generation(
        self,
    ):
        self.commandline.extend(["--disable-mipmap-generation"])

    def with_disable_modal_animations(
        self,
    ):
        self.commandline.extend(["--disable-modal-animations"])

    def with_disable_model_download_verification(
        self,
    ):
        self.commandline.extend(["--disable-model-download-verification"])

    def with_disable_mojo_broker(
        self,
    ):
        self.commandline.extend(["--disable-mojo-broker"])

    def with_disable_mojo_renderer(
        self,
    ):
        self.commandline.extend(["--disable-mojo-renderer"])

    def with_disable_nacl(
        self,
    ):
        self.commandline.extend(["--disable-nacl"])

    def with_disable_namespace_sandbox(
        self,
    ):
        self.commandline.extend(["--disable-namespace-sandbox"])

    def with_disable_new_base_url_inheritance_behavior(
        self,
    ):
        self.commandline.extend(["--disable-new-base-url-inheritance-behavior"])

    def with_disable_new_content_rendering_timeout(
        self,
    ):
        self.commandline.extend(["--disable-new-content-rendering-timeout"])

    def with_disable_notifications(
        self,
    ):
        self.commandline.extend(["--disable-notifications"])

    def with_disable_nv12_dxgi_video(
        self,
    ):
        self.commandline.extend(["--disable-nv12-dxgi-video"])

    def with_disable_oobe_chromevox_hint_timer_for_testing(
        self,
    ):
        self.commandline.extend(["--disable-oobe-chromevox-hint-timer-for-testing"])

    def with_disable_oobe_network_screen_skipping_for_testing(
        self,
    ):
        self.commandline.extend(["--disable-oobe-network-screen-skipping-for-testing"])

    def with_disable_oopr_debug_crash_dump(
        self,
    ):
        self.commandline.extend(["--disable-oopr-debug-crash-dump"])

    def with_disable_origin_trial_controlled_blink_features(
        self,
    ):
        self.commandline.extend(["--disable-origin-trial-controlled-blink-features"])

    def with_disable_overscroll_edge_effect(
        self,
    ):
        self.commandline.extend(["--disable-overscroll-edge-effect"])

    def with_disable_partial_raster(
        self,
    ):
        self.commandline.extend(["--disable-partial-raster"])

    def with_disable_pdf_tagging(
        self,
    ):
        self.commandline.extend(["--disable-pdf-tagging"])

    def with_disable_pepper_3d(
        self,
    ):
        self.commandline.extend(["--disable-pepper-3d"])

    def with_disable_per_user_timezone(
        self,
    ):
        self.commandline.extend(["--disable-per-user-timezone"])

    def with_disable_permissions_api(self):
        self.commandline.extend(["--disable-permissions-api"])

    def with_disable_pinch(self):
        self.commandline.extend(["--disable-pinch"])

    def with_disable_pnacl_crash_throttling(self):
        self.commandline.extend(["--disable-pnacl-crash-throttling"])

    def with_disable_policy_key_verification(self):
        self.commandline.extend(["--disable-policy-key-verification"])

    def with_disable_popup_blocking(self):
        self.commandline.extend(["--disable-popup-blocking"])

    def with_disable_prefer_compositing_to_lcd_text(self):
        self.commandline.extend(["--disable-prefer-compositing-to-lcd-text"])

    def with_disable_presentation_api(self):
        self.commandline.extend(["--disable-presentation-api"])

    def with_disable_print_preview(self):
        self.commandline.extend(["--disable-print-preview"])

    def with_disable_prompt_on_repost(self):
        self.commandline.extend(["--disable-prompt-on-repost"])

    def with_disable_pull_to_refresh_effect(self):
        self.commandline.extend(["--disable-pull-to-refresh-effect"])

    def with_disable_pushstate_throttle(self):
        self.commandline.extend(["--disable-pushstate-throttle"])

    def with_disable_reading_from_canvas(self):
        self.commandline.extend(["--disable-reading-from-canvas"])

    def with_disable_remote_fonts(self):
        self.commandline.extend(["--disable-remote-fonts"])

    def with_disable_remote_playback_api(self):
        self.commandline.extend(["--disable-remote-playback-api"])

    def with_disable_renderer_accessibility(self):
        self.commandline.extend(["--disable-renderer-accessibility"])

    def with_disable_renderer_backgrounding(self):
        self.commandline.extend(["--disable-renderer-backgrounding"])

    def with_disable_resource_scheduler(self):
        self.commandline.extend(["--disable-resource-scheduler"])

    def with_disable_rgba_4444_textures(self):
        self.commandline.extend(["--disable-rgba-4444-textures"])

    def with_disable_rollback_option(self):
        self.commandline.extend(["--disable-rollback-option"])

    def with_disable_rtc_smoothness_algorithm(self):
        self.commandline.extend(["--disable-rtc-smoothness-algorithm"])

    def with_disable_screen_orientation_lock(self):
        self.commandline.extend(["--disable-screen-orientation-lock"])

    def with_disable_scroll_to_text_fragment(self):
        self.commandline.extend(["--disable-scroll-to-text-fragment"])

    def with_disable_search_engine_choice_screen(self):
        self.commandline.extend(["--disable-search-engine-choice-screen"])

    def with_disable_seccomp_filter_sandbox(self):
        self.commandline.extend(["--disable-seccomp-filter-sandbox"])

    def with_disable_setuid_sandbox(self):
        self.commandline.extend(["--disable-setuid-sandbox"])

    def with_disable_shader_name_hashing(self):
        self.commandline.extend(["--disable-shader-name-hashing"])

    def with_disable_shared_workers(self):
        self.commandline.extend(["--disable-shared-workers"])

    def with_disable_signin_frame_client_certs(self):
        self.commandline.extend(["--disable-signin-frame-client-certs"])

    def with_disable_site_isolation_for_policy(self):
        self.commandline.extend(["--disable-site-isolation-for-policy"])

    def with_disable_site_isolation_trials(self):
        self.commandline.extend(["--disable-site-isolation-trials"])

    def with_disable_skia_graphite(self):
        self.commandline.extend(["--disable-skia-graphite"])

    def with_disable_skia_runtime_opts(self):
        self.commandline.extend(["--disable-skia-runtime-opts"])

    def with_disable_smooth_scrolling(self):
        self.commandline.extend(["--disable-smooth-scrolling"])

    def with_disable_software_compositing_fallback(self):
        self.commandline.extend(["--disable-software-compositing-fallback"])

    def with_disable_software_rasterizer(self):
        self.commandline.extend(["--disable-software-rasterizer"])

    def with_disable_speech_api(self):
        self.commandline.extend(["--disable-speech-api"])

    def with_disable_speech_synthesis_api(self):
        self.commandline.extend(["--disable-speech-synthesis-api"])

    def with_disable_stack_profiler(self):
        self.commandline.extend(["--disable-stack-profiler"])

    def with_disable_system_font_check(self):
        self.commandline.extend(["--disable-system-font-check"])

    def with_disable_third_party_keyboard_workaround(self):
        self.commandline.extend(["--disable-third-party-keyboard-workaround"])

    def with_disable_threaded_animation(self):
        self.commandline.extend(["--disable-threaded-animation"])

    def with_disable_threaded_compositing(self):
        self.commandline.extend(["--disable-threaded-compositing"])

    def with_disable_timeouts_for_profiling(self):
        self.commandline.extend(["--disable-timeouts-for-profiling"])

    def with_disable_touch_drag_drop(self):
        self.commandline.extend(["--disable-touch-drag-drop"])

    def with_disable_usb_keyboard_detect(self):
        self.commandline.extend(["--disable-usb-keyboard-detect"])

    def with_disable_v8_idle_tasks(self):
        self.commandline.extend(["--disable-v8-idle-tasks"])

    def with_disable_variations_safe_mode(self):
        self.commandline.extend(["--disable-variations-safe-mode"])

    def with_disable_variations_seed_fetch_throttling(self):
        self.commandline.extend(["--disable-variations-seed-fetch-throttling"])

    def with_disable_video_capture_use_gpu_memory_buffer(self):
        self.commandline.extend(["--disable-video-capture-use-gpu-memory-buffer"])

    def with_disable_virtual_keyboard(self):
        self.commandline.extend(["--disable-virtual-keyboard"])

    def with_disable_volume_adjust_sound(self):
        self.commandline.extend(["--disable-volume-adjust-sound"])

    def with_disable_vsync_for_tests(self):
        self.commandline.extend(["--disable-vsync-for-tests"])

    def with_disable_vulkan_fallback_to_gl_for_testing(self):
        self.commandline.extend(["--disable-vulkan-fallback-to-gl-for-testing"])

    def with_disable_vulkan_for_tests(self):
        self.commandline.extend(["--disable-vulkan-for-tests"])

    def with_disable_vulkan_surface(self):
        self.commandline.extend(["--disable-vulkan-surface"])

    def with_disable_wayland_ime(self):
        self.commandline.extend(["--disable-wayland-ime"])

    def with_disable_web_security(self):
        self.commandline.extend(["--disable-web-security"])

    def with_disable_webgl(self):
        self.commandline.extend(["--disable-webgl"])

    def with_disable_webgl_image_chromium(self):
        self.commandline.extend(["--disable-webgl-image-chromium"])

    def with_disable_webgl2(self):
        self.commandline.extend(["--disable-webgl2"])

    def with_disable_webrtc_encryption(self):
        self.commandline.extend(["--disable-webrtc-encryption"])

    def with_disable_yuv_image_decoding(self):
        self.commandline.extend(["--disable-yuv-image-decoding"])

    def with_disable_zero_browsers_open_for_tests(self):
        self.commandline.extend(["--disable-zero-browsers-open-for-tests"])

    def with_disable_zero_copy(self):
        self.commandline.extend(["--disable-zero-copy"])

    def with_disable_zero_copy_dxgi_video(self):
        self.commandline.extend(["--disable-zero-copy-dxgi-video"])

    def with_disallow_lacros(self):
        self.commandline.extend(["--disallow-lacros"])

    def with_disallow_non_exact_resource_reuse(self):
        self.commandline.extend(["--disallow-non-exact-resource-reuse"])

    def with_disallow_policy_block_dev_mode(self):
        self.commandline.extend(["--disallow-policy-block-dev-mode"])

    def with_discoverability(self):
        self.commandline.extend(["--discoverability"])

    def with_document_user_activation_required(self):
        self.commandline.extend(["--document-user-activation-required"])

    def with_dom_automation(self):
        self.commandline.extend(["--dom-automation"])

    def with_double_buffer_compositing(self):
        self.commandline.extend(["--double-buffer-compositing"])

    def with_draw_quad_split_limit(self):
        self.commandline.extend(["--draw-quad-split-limit"])

    def with_draw_view_bounds_rects(self):
        self.commandline.extend(["--draw-view-bounds-rects"])

    def with_drm_virtual_connector_is_external(self):
        self.commandline.extend(["--drm-virtual-connector-is-external"])

    def with_dump_blink_runtime_call_stats(self):
        self.commandline.extend(["--dump-blink-runtime-call-stats"])

    def with_dump_browser_histograms(self):
        self.commandline.extend(["--dump-browser-histograms"])

    def with_dump_dom(self):
        self.commandline.extend(["--dump-dom"])

    def with_dumpstate_path(self):
        self.commandline.extend(["--dumpstate-path"])

    def with_edge_touch_filtering(self):
        self.commandline.extend(["--edge-touch-filtering"])

    def with_egl(self):
        self.commandline.extend(["--egl"])

    def with_elevate(self):
        self.commandline.extend(["--elevate"])

    def with_embedded_extension_options(self):
        self.commandline.extend(["--embedded-extension-options"])

    def with_enable(self):
        self.commandline.extend(["--enable"])

    def with_enable_accelerated_2d_canvas(self):
        self.commandline.extend(["--enable-accelerated-2d-canvas"])

    def with_enable_adaptive_selection_handle_orientation(self):
        self.commandline.extend(["--enable-adaptive-selection-handle-orientation"])

    def with_enable_aggressive_domstorage_flushing(self):
        self.commandline.extend(["--enable-aggressive-domstorage-flushing"])

    def with_enable_angle_features(self):
        self.commandline.extend(["--enable-angle-features"])

    def with_enable_arc(self):
        self.commandline.extend(["--enable-arc"])

    def with_enable_arcvm(self):
        self.commandline.extend(["--enable-arcvm"])

    def with_enable_arcvm_rt_vcpu(self):
        self.commandline.extend(["--enable-arcvm-rt-vcpu"])

    def with_enable_ash_debug_browser(self):
        self.commandline.extend(["--enable-ash-debug-browser"])

    def with_enable_audio_debug_recordings_from_extension(self):
        self.commandline.extend(["--enable-audio-debug-recordings-from-extension"])

    def with_enable_auto_reload(self):
        self.commandline.extend(["--enable-auto-reload"])

    def with_enable_automation(self):
        self.commandline.extend(["--enable-automation"])

    def with_enable_background_thread_pool(self):
        self.commandline.extend(["--enable-background-thread-pool"])

    def with_enable_background_tracing(self):
        self.commandline.extend(["--enable-background-tracing"])

    def with_enable_begin_frame_control(self):
        self.commandline.extend(["--enable-begin-frame-control"])

    def with_enable_benchmarking(self):
        self.commandline.extend(["--enable-benchmarking"])

    def with_enable_ble_advertising_in_apps(self):
        self.commandline.extend(["--enable-ble-advertising-in-apps"])

    def with_enable_blink_features(self):
        self.commandline.extend(["--enable-blink-features"])

    def with_enable_blink_test_features(self):
        self.commandline.extend(["--enable-blink-test-features"])

    def with_enable_bookmark_undo(self):
        self.commandline.extend(["--enable-bookmark-undo"])

    def with_enable_caret_browsing(self):
        self.commandline.extend(["--enable-caret-browsing"])

    def with_enable_cast_receiver(self):
        self.commandline.extend(["--enable-cast-receiver"])

    def with_enable_cast_streaming_receiver(self):
        self.commandline.extend(["--enable-cast-streaming-receiver"])

    def with_enable_chrome_browser_cloud_management(self):
        self.commandline.extend(["--enable-chrome-browser-cloud-management"])

    def with_enable_cloud_print_proxy(self):
        self.commandline.extend(["--enable-cloud-print-proxy"])

    def with_enable_consumer_kiosk(self):
        self.commandline.extend(["--enable-consumer-kiosk"])

    def with_enable_content_directories(self):
        self.commandline.extend(["--enable-content-directories"])

    def with_enable_crash_reporter(self):
        self.commandline.extend(["--enable-crash-reporter"])

    def with_enable_crash_reporter_for_testing(self):
        self.commandline.extend(["--enable-crash-reporter-for-testing"])

    def with_enable_crx_hash_check(self):
        self.commandline.extend(["--enable-crx-hash-check"])

    def with_enable_dawn_backend_validation(self):
        self.commandline.extend(["--enable-dawn-backend-validation"])

    def with_enable_dawn_features(self):
        self.commandline.extend(["--enable-dawn-features"])

    def with_enable_dim_shelf(self):
        self.commandline.extend(["--enable-dim-shelf"])

    def with_enable_dinosaur_easter_egg_alt_images(self):
        self.commandline.extend(["--enable-dinosaur-easter-egg-alt-images"])

    def with_enable_direct_composition_video_overlays(self):
        self.commandline.extend(["--enable-direct-composition-video-overlays"])

    def with_enable_discover_feed(self):
        self.commandline.extend(["--enable-discover-feed"])

    def with_enable_distillability_service(self):
        self.commandline.extend(["--enable-distillability-service"])

    def with_enable_dom_distiller(self):
        self.commandline.extend(["--enable-dom-distiller"])

    def with_enable_domain_reliability(self):
        self.commandline.extend(["--enable-domain-reliability"])

    def with_enable_download_warning_improvements(self):
        self.commandline.extend(["--enable-download-warning-improvements"])

    def with_enable_encryption_selection(self):
        self.commandline.extend(["--enable-encryption-selection"])

    def with_enable_exclusive_audio(self):
        self.commandline.extend(["--enable-exclusive-audio"])

    def with_enable_experimental_accessibility_autoclick(self):
        self.commandline.extend(["--enable-experimental-accessibility-autoclick"])

    def with_enable_experimental_accessibility_labels_debugging(self):
        self.commandline.extend(
            ["--enable-experimental-accessibility-labels-debugging"]
        )

    def with_enable_experimental_accessibility_language_detection(self):
        self.commandline.extend(
            ["--enable-experimental-accessibility-language-detection"]
        )

    def with_enable_experimental_accessibility_language_detection_dynamic(self):
        self.commandline.extend(
            ["--enable-experimental-accessibility-language-detection-dynamic"]
        )

    def with_enable_experimental_accessibility_manifest_v3(self):
        self.commandline.extend(["--enable-experimental-accessibility-manifest-v3"])

    def with_enable_experimental_accessibility_switch_access_text(self):
        self.commandline.extend(
            ["--enable-experimental-accessibility-switch-access-text"]
        )

    def with_enable_experimental_cookie_features(self):
        self.commandline.extend(["--enable-experimental-cookie-features"])

    def with_enable_experimental_extension_apis(self):
        self.commandline.extend(["--enable-experimental-extension-apis"])

    def with_enable_experimental_web_platform_features(self):
        self.commandline.extend(["--enable-experimental-web-platform-features"])

    def with_enable_experimental_webassembly_features(self):
        self.commandline.extend(["--enable-experimental-webassembly-features"])

    def with_enable_extension_activity_log_testing(self):
        self.commandline.extend(["--enable-extension-activity-log-testing"])

    def with_enable_extension_activity_logging(self):
        self.commandline.extend(["--enable-extension-activity-logging"])

    def with_enable_extension_assets_sharing(self):
        self.commandline.extend(["--enable-extension-assets-sharing"])

    def with_enable_fake_no_alloc_direct_call_for_testing(self):
        self.commandline.extend(["--enable-fake-no-alloc-direct-call-for-testing"])

    def with_enable_features(self):
        self.commandline.extend(["--enable-features"])

    def with_enable_field_trial_config(self):
        self.commandline.extend(["--enable-field-trial-config"])

    def with_enable_finch_seed_delta_compression(self):
        self.commandline.extend(["--enable-finch-seed-delta-compression"])

    def with_enable_font_antialiasing(self):
        self.commandline.extend(["--enable-font-antialiasing"])

    def with_enable_gamepad_button_axis_events(self):
        self.commandline.extend(["--enable-gamepad-button-axis-events"])

    def with_enable_gpu(self):
        self.commandline.extend(["--enable-gpu"])

    def with_enable_gpu_benchmarking(self):
        self.commandline.extend(["--enable-gpu-benchmarking"])

    def with_enable_gpu_blocked_time(self):
        self.commandline.extend(["--enable-gpu-blocked-time"])

    def with_enable_gpu_client_logging(self):
        self.commandline.extend(["--enable-gpu-client-logging"])

    def with_enable_gpu_client_tracing(self):
        self.commandline.extend(["--enable-gpu-client-tracing"])

    def with_enable_gpu_command_logging(self):
        self.commandline.extend(["--enable-gpu-command-logging"])

    def with_enable_gpu_debugging(self):
        self.commandline.extend(["--enable-gpu-debugging"])

    def with_enable_gpu_driver_debug_logging(self):
        self.commandline.extend(["--enable-gpu-driver-debug-logging"])

    def with_enable_gpu_memory_buffer_compositor_resources(self):
        self.commandline.extend(["--enable-gpu-memory-buffer-compositor-resources"])

    def with_enable_gpu_memory_buffer_video_frames(self):
        self.commandline.extend(["--enable-gpu-memory-buffer-video-frames"])

    def with_enable_gpu_rasterization(self):
        self.commandline.extend(["--enable-gpu-rasterization"])

    def with_enable_gpu_service_logging(self):
        self.commandline.extend(["--enable-gpu-service-logging"])

    def with_enable_gpu_service_tracing(self):
        self.commandline.extend(["--enable-gpu-service-tracing"])

    def with_enable_hangout_services_extension_for_testing(self):
        self.commandline.extend(["--enable-hangout-services-extension-for-testing"])

    def with_enable_hardware_overlays(self):
        self.commandline.extend(["--enable-hardware-overlays"])

    def with_enable_houdini(self):
        self.commandline.extend(["--enable-houdini"])

    def with_enable_houdini_dlc(self):
        self.commandline.extend(["--enable-houdini-dlc"])

    def with_enable_houdini64(self):
        self.commandline.extend(["--enable-houdini64"])

    def with_enable_idle_tracing(self):
        self.commandline.extend(["--enable-idle-tracing"])

    def with_enable_input(self):
        self.commandline.extend(["--enable-input"])

    def with_enable_ios_handoff_to_other_devices(self):
        self.commandline.extend(["--enable-ios-handoff-to-other-devices"])

    def with_enable_isolated_web_apps_in_renderer(self):
        self.commandline.extend(["--enable-isolated-web-apps-in-renderer"])

    def with_enable_lacros_fork_zygotes_at_login_screen(self):
        self.commandline.extend(["--enable-lacros-fork-zygotes-at-login-screen"])

    def with_enable_lcd_text(self):
        self.commandline.extend(["--enable-lcd-text"])

    def with_enable_leak_detection(self):
        self.commandline.extend(["--enable-leak-detection"])

    def with_enable_leak_detection_heap_snapshot(self):
        self.commandline.extend(["--enable-leak-detection-heap-snapshot"])

    def with_enable_legacy_background_tracing(self):
        self.commandline.extend(["--enable-legacy-background-tracing"])

    def with_enable_live_caption_pref_for_testing(self):
        self.commandline.extend(["--enable-live-caption-pref-for-testing"])

    def with_enable_local_file_accesses(self):
        self.commandline.extend(["--enable-local-file-accesses"])

    def with_enable_logging(self):
        self.commandline.extend(["--enable-logging"])

    def with_enable_longpress_drag_selection(self):
        self.commandline.extend(["--enable-longpress-drag-selection"])

    def with_enable_low_end_device_mode(self):
        self.commandline.extend(["--enable-low-end-device-mode"])

    def with_enable_low_res_tiling(self):
        self.commandline.extend(["--enable-low-res-tiling"])

    def with_enable_magnifier_debug_draw_rect(self):
        self.commandline.extend(["--enable-magnifier-debug-draw-rect"])

    def with_enable_main_frame_before_activation(self):
        self.commandline.extend(["--enable-main-frame-before-activation"])

    def with_enable_nacl(self):
        self.commandline.extend(["--enable-nacl"])

    def with_enable_nacl_debug(self):
        self.commandline.extend(["--enable-nacl-debug"])

    def with_enable_native_gpu_memory_buffers(self):
        self.commandline.extend(["--enable-native-gpu-memory-buffers"])

    def with_enable_natural_scroll_default(self):
        self.commandline.extend(["--enable-natural-scroll-default"])

    def with_enable_ndk_translation(self):
        self.commandline.extend(["--enable-ndk-translation"])

    def with_enable_ndk_translation64(self):
        self.commandline.extend(["--enable-ndk-translation64"])

    def with_enable_net_benchmarking(self):
        self.commandline.extend(["--enable-net-benchmarking"])

    def with_enable_network_information_downlink_max(self):
        self.commandline.extend(["--enable-network-information-downlink-max"])

    def with_enable_new_app_menu_icon(self):
        self.commandline.extend(["--enable-new-app-menu-icon"])

    def with_enable_ntp_search_engine_country_detection(self):
        self.commandline.extend(["--enable-ntp-search-engine-country-detection"])

    def with_enable_oobe_chromevox_hint_timer_for_dev_mode(self):
        self.commandline.extend(["--enable-oobe-chromevox-hint-timer-for-dev-mode"])

    def with_enable_oobe_test_api(self):
        self.commandline.extend(["--enable-oobe-test-api"])

    def with_enable_optimization_guide_debug_logs(self):
        self.commandline.extend(["--enable-optimization-guide-debug-logs"])

    def with_enable_page_content_annotations_logging(self):
        self.commandline.extend(["--enable-page-content-annotations-logging"])

    def with_enable_pepper_testing(self):
        self.commandline.extend(["--enable-pepper-testing"])

    def with_enable_pixel_output_in_tests(self):
        self.commandline.extend(["--enable-pixel-output-in-tests"])

    def with_enable_plugin_placeholder_testing(self):
        self.commandline.extend(["--enable-plugin-placeholder-testing"])

    def with_enable_potentially_annoying_security_features(self):
        self.commandline.extend(["--enable-potentially-annoying-security-features"])

    def with_enable_precise_memory_info(self):
        self.commandline.extend(["--enable-precise-memory-info"])

    def with_enable_prefer_compositing_to_lcd_text(self):
        self.commandline.extend(["--enable-prefer-compositing-to-lcd-text"])

    def with_enable_primary_node_access_for_vkms_testing(self):
        self.commandline.extend(["--enable-primary-node-access-for-vkms-testing"])

    def with_enable_privacy_sandbox_ads_apis(self):
        self.commandline.extend(["--enable-privacy-sandbox-ads-apis"])

    def with_enable_profile_shortcut_manager(self):
        self.commandline.extend(["--enable-profile-shortcut-manager"])

    def with_enable_promo_manager_fullscreen_promos(self):
        self.commandline.extend(["--enable-promo-manager-fullscreen-promos"])

    def with_enable_protected_video_buffers(self):
        self.commandline.extend(["--enable-protected-video-buffers"])

    def with_enable_raster_side_dark_mode_for_images(self):
        self.commandline.extend(["--enable-raster-side-dark-mode-for-images"])

    def with_enable_requisition_edits(self):
        self.commandline.extend(["--enable-requisition-edits"])

    def with_enable_resources_file_sharing(self):
        self.commandline.extend(["--enable-resources-file-sharing"])

    def with_enable_rgba_4444_textures(self):
        self.commandline.extend(["--enable-rgba-4444-textures"])

    def with_enable_sandbox_logging(self):
        self.commandline.extend(["--enable-sandbox-logging"])

    def with_enable_scaling_clipped_images(self):
        self.commandline.extend(["--enable-scaling-clipped-images"])

    def with_enable_service_binary_launcher(self):
        self.commandline.extend(["--enable-service-binary-launcher"])

    def with_enable_service_manager_tracing(self):
        self.commandline.extend(["--enable-service-manager-tracing"])

    def with_enable_sgi_video_sync(self):
        self.commandline.extend(["--enable-sgi-video-sync"])

    def with_enable_skia_benchmarking(self):
        self.commandline.extend(["--enable-skia-benchmarking"])

    def with_enable_skia_graphite(self):
        self.commandline.extend(["--enable-skia-graphite"])

    def with_enable_smooth_scrolling(self):
        self.commandline.extend(["--enable-smooth-scrolling"])

    def with_enable_spatial_navigation(self):
        self.commandline.extend(["--enable-spatial-navigation"])

    def with_enable_speech_dispatcher(self):
        self.commandline.extend(["--enable-speech-dispatcher"])

    def with_enable_spotlight_actions(self):
        self.commandline.extend(["--enable-spotlight-actions"])

    def with_enable_stats_collection_bindings(self):
        self.commandline.extend(["--enable-stats-collection-bindings"])

    def with_enable_strict_mixed_content_checking(self):
        self.commandline.extend(["--enable-strict-mixed-content-checking"])

    def with_enable_strict_powerful_feature_restrictions(self):
        self.commandline.extend(["--enable-strict-powerful-feature-restrictions"])

    def with_enable_swap_buffers_with_bounds(self):
        self.commandline.extend(["--enable-swap-buffers-with-bounds"])

    def with_enable_tablet_form_factor(self):
        self.commandline.extend(["--enable-tablet-form-factor"])

    def with_enable_third_party_keyboard_workaround(self):
        self.commandline.extend(["--enable-third-party-keyboard-workaround"])

    def with_enable_threaded_texture_mailboxes(self):
        self.commandline.extend(["--enable-threaded-texture-mailboxes"])

    def with_enable_top_drag_gesture(self):
        self.commandline.extend(["--enable-top-drag-gesture"])

    def with_enable_touch_calibration_setting(self):
        self.commandline.extend(["--enable-touch-calibration-setting"])

    def with_enable_touch_drag_drop(self):
        self.commandline.extend(["--enable-touch-drag-drop"])

    def with_enable_touchpad_three_finger_click(self):
        self.commandline.extend(["--enable-touchpad-three-finger-click"])

    def with_enable_touchview(self):
        self.commandline.extend(["--enable-touchview"])

    def with_enable_trace_app_source(self):
        self.commandline.extend(["--enable-trace-app-source"])

    def with_enable_tracing(self):
        self.commandline.extend(["--enable-tracing"])

    def with_enable_tracing_format(self):
        self.commandline.extend(["--enable-tracing-format"])

    def with_enable_tracing_fraction(self):
        self.commandline.extend(["--enable-tracing-fraction"])

    def with_enable_tracing_output(self):
        self.commandline.extend(["--enable-tracing-output"])

    def with_enable_ui_devtools(self):
        self.commandline.extend(["--enable-ui-devtools"])

    def with_enable_unsafe_webgpu(self):
        self.commandline.extend(["--enable-unsafe-webgpu"])

    def with_enable_upgrade_signin_promo(self):
        self.commandline.extend(["--enable-upgrade-signin-promo"])

    def with_enable_user_metrics(self):
        self.commandline.extend(["--enable-user-metrics"])

    def with_enable_usermedia_screen_capturing(self):
        self.commandline.extend(["--enable-usermedia-screen-capturing"])

    def with_enable_viewport(self):
        self.commandline.extend(["--enable-viewport"])

    def with_enable_virtual_keyboard(self):
        self.commandline.extend(["--enable-virtual-keyboard"])

    def with_enable_vtune_support(self):
        self.commandline.extend(["--enable-vtune-support"])

    def with_enable_vulkan_protected_memory(self):
        self.commandline.extend(["--enable-vulkan-protected-memory"])

    def with_enable_wayland_ime(self):
        self.commandline.extend(["--enable-wayland-ime"])

    def with_enable_wayland_server(self):
        self.commandline.extend(["--enable-wayland-server"])

    def with_enable_web_auth_deprecated_mojo_testing_api(self):
        self.commandline.extend(["--enable-web-auth-deprecated-mojo-testing-api"])

    def with_enable_webgl_developer_extensions(self):
        self.commandline.extend(["--enable-webgl-developer-extensions"])

    def with_enable_webgl_draft_extensions(self):
        self.commandline.extend(["--enable-webgl-draft-extensions"])

    def with_enable_webgl_image_chromium(self):
        self.commandline.extend(["--enable-webgl-image-chromium"])

    def with_enable_webgpu_developer_features(self):
        self.commandline.extend(["--enable-webgpu-developer-features"])

    def with_enable_webrtc_srtp_encrypted_headers(self):
        self.commandline.extend(["--enable-webrtc-srtp-encrypted-headers"])

    def with_enable_widevine(self):
        self.commandline.extend(["--enable-widevine"])

    def with_enable_zero_copy(self):
        self.commandline.extend(["--enable-zero-copy"])

    def with_enabled(self):
        self.commandline.extend(["--enabled"])

    def with_encode_binary(self):
        self.commandline.extend(["--encode-binary"])

    def with_encrypted_reporting_url(self):
        self.commandline.extend(["--encrypted-reporting-url"])

    def with_enforce(self):
        self.commandline.extend(["--enforce"])

    def with_enforce_gl_minimums(self):
        self.commandline.extend(["--enforce-gl-minimums"])

    def with_enforce_webrtc_ip_permission_check(self):
        self.commandline.extend(["--enforce-webrtc-ip-permission-check"])

    def with_enforce_strict(self):
        self.commandline.extend(["--enforce-strict"])

    def with_ensure_forced_color_profile(self):
        self.commandline.extend(["--ensure-forced-color-profile"])

    def with_enterprise_disable_arc(self):
        self.commandline.extend(["--enterprise-disable-arc"])

    def with_enterprise_enable_forced_re_enrollment(self):
        self.commandline.extend(["--enterprise-enable-forced-re-enrollment"])

    def with_enterprise_enable_forced_re_enrollment_on_flex(self):
        self.commandline.extend(["--enterprise-enable-forced-re-enrollment-on-flex"])

    def with_enterprise_enable_initial_enrollment(self):
        self.commandline.extend(["--enterprise-enable-initial-enrollment"])

    def with_enterprise_enable_unified_state_determination(self):
        self.commandline.extend(["--enterprise-enable-unified-state-determination"])

    def with_enterprise_enable_zero_touch_enrollment(self):
        self.commandline.extend(["--enterprise-enable-zero-touch-enrollment"])

    def with_enterprise_enrollment_initial_modulus(self):
        self.commandline.extend(["--enterprise-enrollment-initial-modulus"])

    def with_enterprise_enrollment_modulus_limit(self):
        self.commandline.extend(["--enterprise-enrollment-modulus-limit"])

    def with_enterprise_force_manual_enrollment_in_test_builds(self):
        self.commandline.extend(["--enterprise-force-manual-enrollment-in-test-builds"])

    def with_eol_ignore_profile_creation_time(self):
        self.commandline.extend(["--eol-ignore-profile-creation-time"])

    def with_eol_reset_dismissed_prefs(self):
        self.commandline.extend(["--eol-reset-dismissed-prefs"])

    def with_evaluate_type(self):
        self.commandline.extend(["--evaluate-type"])

    def with_evaluate_capability(self):
        self.commandline.extend(["--evaluate-capability"])

    def with_explicitly_allowed_ports(self):
        self.commandline.extend(["--explicitly-allowed-ports"])

    def with_export_uma_logs_to_file(self):
        self.commandline.extend(["--export-uma-logs-to-file"])

    def with_expose_internals_for_testing(self):
        self.commandline.extend(["--expose-internals-for-testing"])

    def with_extension_apps_block_for_app_service_in_ash(self):
        self.commandline.extend(["--extension-apps-block-for-app-service-in-ash"])

    def with_extension_apps_run_in_ash_and_lacros(self):
        self.commandline.extend(["--extension-apps-run-in-ash-and-lacros"])

    def with_extension_apps_run_in_ash_only(self):
        self.commandline.extend(["--extension-apps-run-in-ash-only"])

    def with_extension_content_verification(self):
        self.commandline.extend(["--extension-content-verification"])

    def with_extension_force_channel(self):
        self.commandline.extend(["--extension-force-channel"])

    def with_extension_install_event_chrome_log_for_tests(self):
        self.commandline.extend(["--extension-install-event-chrome-log-for-tests"])

    def with_extension_process(self):
        self.commandline.extend(["--extension-process"])

    def with_extension_updater_test_request(self):
        self.commandline.extend(["--extension-updater-test-request"])

    def with_extensions_install_verification(self):
        self.commandline.extend(["--extensions-install-verification"])

    def with_extensions_not_webstore(self):
        self.commandline.extend(["--extensions-not-webstore"])

    def with_extensions_on_chrome_urls(self):
        self.commandline.extend(["--extensions-on-chrome-urls"])

    def with_extensions_run_in_ash_and_lacros(self):
        self.commandline.extend(["--extensions-run-in-ash-and-lacros"])

    def with_extensions_run_in_ash_only(self):
        self.commandline.extend(["--extensions-run-in-ash-only"])

    def with_external_metrics_collection_interval(self):
        self.commandline.extend(["--external-metrics-collection-interval"])

    def with_extra_search_query_params(self):
        self.commandline.extend(["--extra-search-query-params"])

    def with_extra_web_apps_dir(self):
        self.commandline.extend(["--extra-web-apps-dir"])

    def with_fail_audio_stream_creation(self):
        self.commandline.extend(["--fail-audio-stream-creation"])

    def with_fake_arc_recommended_apps_for_testing(self):
        self.commandline.extend(["--fake-arc-recommended-apps-for-testing"])

    def with_fake_drivefs_launcher_chroot_path(self):
        self.commandline.extend(["--fake-drivefs-launcher-chroot-path"])

    def with_fake_drivefs_launcher_socket_path(self):
        self.commandline.extend(["--fake-drivefs-launcher-socket-path"])

    def with_fake_oobe_configuration_file(self):
        self.commandline.extend(["--fake-oobe-configuration-file"])

    def with_fake_variations_channel(self):
        self.commandline.extend(["--fake-variations-channel"])

    def with_false(self):
        self.commandline.extend(["--false"])

    def with_feedback_server(self):
        self.commandline.extend(["--feedback-server"])

    def with_field_trial_handle(self):
        self.commandline.extend(["--field-trial-handle"])

    def with_file_storage_server_upload_url(self):
        self.commandline.extend(["--file-storage-server-upload-url"])

    def with_file_url_path_alias(self):
        self.commandline.extend(["--file-url-path-alias"])

    def with_file_chooser(self):
        self.commandline.extend(["--file-chooser"])

    def with_finch_seed_expiration_age(self):
        self.commandline.extend(["--finch-seed-expiration-age"])

    def with_finch_seed_ignore_pending_download(self):
        self.commandline.extend(["--finch-seed-ignore-pending-download"])

    def with_finch_seed_min_download_period(self):
        self.commandline.extend(["--finch-seed-min-download-period"])

    def with_finch_seed_min_update_period(self):
        self.commandline.extend(["--finch-seed-min-update-period"])

    def with_finch_seed_no_charging_requirement(self):
        self.commandline.extend(["--finch-seed-no-charging-requirement"])

    def with_fingerprint_sensor_location(self):
        self.commandline.extend(["--fingerprint-sensor-location"])

    def with_first_exec_after_boot(self):
        self.commandline.extend(["--first-exec-after-boot"])

    def with_flag_switches_begin(self):
        self.commandline.extend(["--flag-switches-begin"])

    def with_flag_switches_end(self):
        self.commandline.extend(["--flag-switches-end"])

    def with_font_cache_shared_handle(self):
        self.commandline.extend(["--font-cache-shared-handle"])

    def with_font_render_hinting(self):
        self.commandline.extend(["--font-render-hinting"])

    def with_force_app_mode(self):
        self.commandline.extend(["--force-app-mode"])

    def with_force_assistant_onboarding(self):
        self.commandline.extend(["--force-assistant-onboarding"])

    def with_force_birch_fetch(self):
        self.commandline.extend(["--force-birch-fetch"])

    def with_force_birch_release_notes(self):
        self.commandline.extend(["--force-birch-release-notes"])

    def with_force_browser_crash_on_gpu_crash(self):
        self.commandline.extend(["--force-browser-crash-on-gpu-crash"])

    def with_force_browser_data_migration_for_testing(self):
        self.commandline.extend(["--force-browser-data-migration-for-testing"])

    def with_force_caption_style(self):
        self.commandline.extend(["--force-caption-style"])

    def with_force_color_profile(self):
        self.commandline.extend(["--force-color-profile"])

    def with_force_cryptohome_recovery_for_testing(self):
        self.commandline.extend(["--force-cryptohome-recovery-for-testing"])

    def with_force_dark_mode(self):
        self.commandline.extend(["--force-dark-mode"])

    def with_force_dev_mode_highlighting(self):
        self.commandline.extend(["--force-dev-mode-highlighting"])

    def with_force_device_ownership(self):
        self.commandline.extend(["--force-device-ownership"])

    def with_force_device_scale_factor(self):
        self.commandline.extend(["--force-device-scale-factor"])

    def with_force_device_switcher_experience(self):
        self.commandline.extend(["--force-device-switcher-experience"])

    def with_force_devtools_available(self):
        self.commandline.extend(["--force-devtools-available"])

    def with_force_disable_variation_ids(self):
        self.commandline.extend(["--force-disable-variation-ids"])

    def with_force_effective_connection_type(self):
        self.commandline.extend(["--force-effective-connection-type"])

    def with_force_enable_metrics_reporting(self):
        self.commandline.extend(["--force-enable-metrics-reporting"])

    def with_force_enable_night_mode(self):
        self.commandline.extend(["--force-enable-night-mode"])

    def with_force_enable_stylus_tools(self):
        self.commandline.extend(["--force-enable-stylus-tools"])

    def with_force_fieldtrial_params(self):
        self.commandline.extend(["--force-fieldtrial-params"])

    def with_force_fieldtrials(self):
        self.commandline.extend(["--force-fieldtrials"])

    def with_force_first_run(self):
        self.commandline.extend(["--force-first-run"])

    def with_force_first_run_ui(self):
        self.commandline.extend(["--force-first-run-ui"])

    def with_force_gpu_mem_available_mb(self):
        self.commandline.extend(["--force-gpu-mem-available-mb"])

    def with_force_gpu_mem_discardable_limit_mb(self):
        self.commandline.extend(["--force-gpu-mem-discardable-limit-mb"])

    def with_force_happiness_tracking_system(self):
        self.commandline.extend(["--force-happiness-tracking-system"])

    def with_force_headless_for_tests(self):
        self.commandline.extend(["--force-headless-for-tests"])

    def with_force_high_contrast(self):
        self.commandline.extend(["--force-high-contrast"])

    def with_force_hwid_check_result_for_test(self):
        self.commandline.extend(["--force-hwid-check-result-for-test"])

    def with_force_lacros_launch_at_login_screen_for_testing(self):
        self.commandline.extend(["--force-lacros-launch-at-login-screen-for-testing"])

    def with_force_launch_browser(self):
        self.commandline.extend(["--force-launch-browser"])

    def with_force_login_manager_in_tests(self):
        self.commandline.extend(["--force-login-manager-in-tests"])

    def with_force_max_texture_size(self):
        self.commandline.extend(["--force-max-texture-size"])

    def with_force_media_resolution_height(self):
        self.commandline.extend(["--force-media-resolution-height"])

    def with_force_media_resolution_width(self):
        self.commandline.extend(["--force-media-resolution-width"])

    def with_force_msbb_setting_on_for_ukm(self):
        self.commandline.extend(["--force-msbb-setting-on-for-ukm"])

    def with_force_online_connection_state_for_indicator(self):
        self.commandline.extend(["--force-online-connection-state-for-indicator"])

    def with_force_permission_policy_unload_default_enabled(self):
        self.commandline.extend(["--force-permission-policy-unload-default-enabled"])

    def with_force_pnacl_subzero(self):
        self.commandline.extend(["--force-pnacl-subzero"])

    def with_force_prefers_no_reduced_motion(self):
        self.commandline.extend(["--force-prefers-no-reduced-motion"])

    def with_force_prefers_reduced_motion(self):
        self.commandline.extend(["--force-prefers-reduced-motion"])

    def with_force_presentation_receiver_for_testing(self):
        self.commandline.extend(["--force-presentation-receiver-for-testing"])

    def with_force_protected_video_output_buffers(self):
        self.commandline.extend(["--force-protected-video-output-buffers"])

    def with_force_raster_color_profile(self):
        self.commandline.extend(["--force-raster-color-profile"])

    def with_force_refresh_rate_throttle(self):
        self.commandline.extend(["--force-refresh-rate-throttle"])

    def with_force_renderer_accessibility(self):
        self.commandline.extend(["--force-renderer-accessibility"])

    def with_force_search_engine_choice_screen(self):
        self.commandline.extend(["--force-search-engine-choice-screen"])

    def with_force_separate_egl_display_for_webgl_testing(self):
        self.commandline.extend(["--force-separate-egl-display-for-webgl-testing"])

    def with_force_show_cursor(self):
        self.commandline.extend(["--force-show-cursor"])

    def with_force_show_release_track(self):
        self.commandline.extend(["--force-show-release-track"])

    def with_force_show_update_menu_badge(self):
        self.commandline.extend(["--force-show-update-menu-badge"])

    def with_force_status_area_collapsible(self):
        self.commandline.extend(["--force-status-area-collapsible"])

    def with_force_tablet_mode(self):
        self.commandline.extend(["--force-tablet-mode"])

    def with_force_tablet_power_button(self):
        self.commandline.extend(["--force-tablet-power-button"])

    def with_force_text_direction(self):
        self.commandline.extend(["--force-text-direction"])

    def with_force_ui_direction(self):
        self.commandline.extend(["--force-ui-direction"])

    def with_force_update_menu_type(self):
        self.commandline.extend(["--force-update-menu-type"])

    def with_force_update_remote_url(self):
        self.commandline.extend(["--force-update-remote-url"])

    def with_force_variation_ids(self):
        self.commandline.extend(["--force-variation-ids"])

    def with_force_video_overlays(self):
        self.commandline.extend(["--force-video-overlays"])

    def with_force_wave_audio(self):
        self.commandline.extend(["--force-wave-audio"])

    def with_force_webgpu_compat(self):
        self.commandline.extend(["--force-webgpu-compat"])

    def with_force_webrtc_ip_handling_policy(self):
        self.commandline.extend(["--force-webrtc-ip-handling-policy"])

    def with_force_webxr_runtime(self):
        self.commandline.extend(["--force-webxr-runtime"])

    def with_force_whats_new(self):
        self.commandline.extend(["--force-whats-new"])

    def with_forest_feature_key(self):
        self.commandline.extend(["--forest-feature-key"])

    def with_form_factor(self):
        self.commandline.extend(["--form-factor"])

    def with_full_memory_crash_report(self):
        self.commandline.extend(["--full-memory-crash-report"])

    def with_gaia_config(self):
        self.commandline.extend(["--gaia-config"])

    def with_gaia_config_contents(self):
        self.commandline.extend(["--gaia-config-contents"])

    def with_gaia_url(self):
        self.commandline.extend(["--gaia-url"])

    def with_gamepad_polling_interval(self):
        self.commandline.extend(["--gamepad-polling-interval"])

    def with_gcm_checkin_url(self):
        self.commandline.extend(["--gcm-checkin-url"])

    def with_gcm_mcs_endpoint(self):
        self.commandline.extend(["--gcm-mcs-endpoint"])

    def with_gcm_registration_url(self):
        self.commandline.extend(["--gcm-registration-url"])

    def with_generate_accessibility_test_expectations(self):
        self.commandline.extend(["--generate-accessibility-test-expectations"])

    def with_generate_pdf_document_outline(self):
        self.commandline.extend(["--generate-pdf-document-outline"])

    def with_get_access_token_for_test(self):
        self.commandline.extend(["--get-access-token-for-test"])

    def with_gl(self):
        self.commandline.extend(["--gl"])

    def with_gl_egl(self):
        self.commandline.extend(["--gl-egl"])

    def with_gl_null(self):
        self.commandline.extend(["--gl-null"])

    def with_gl_shader_interm_output(self):
        self.commandline.extend(["--gl-shader-interm-output"])

    def with_glanceables_key(self):
        self.commandline.extend(["--glanceables-key"])

    def with_gles(self):
        self.commandline.extend(["--gles"])

    def with_gles_egl(self):
        self.commandline.extend(["--gles-egl"])

    def with_gles_null(self):
        self.commandline.extend(["--gles-null"])

    def with_google_api_key(self):
        self.commandline.extend(["--google-api-key"])

    def with_google_apis_url(self):
        self.commandline.extend(["--google-apis-url"])

    def with_google_base_url(self):
        self.commandline.extend(["--google-base-url"])

    def with_google_doodle_url(self):
        self.commandline.extend(["--google-doodle-url"])

    def with_gpu(self):
        self.commandline.extend(["--gpu"])

    def with_gpu_blocklist_test_group(self):
        self.commandline.extend(["--gpu-blocklist-test-group"])

    def with_gpu_device_id(self):
        self.commandline.extend(["--gpu-device-id"])

    def with_gpu_disk_cache_size_kb(self):
        self.commandline.extend(["--gpu-disk-cache-size-kb"])

    def with_gpu_driver_bug_list_test_group(self):
        self.commandline.extend(["--gpu-driver-bug-list-test-group"])

    def with_gpu_driver_version(self):
        self.commandline.extend(["--gpu-driver-version"])

    def with_gpu_launcher(self):
        self.commandline.extend(["--gpu-launcher"])

    def with_gpu_no_context_lost(self):
        self.commandline.extend(["--gpu-no-context-lost"])

    def with_gpu_preferences(self):
        self.commandline.extend(["--gpu-preferences"])

    def with_gpu_process(self):
        self.commandline.extend(["--gpu-process"])

    def with_gpu_program_cache_size_kb(self):
        self.commandline.extend(["--gpu-program-cache-size-kb"])

    def with_gpu_rasterization_msaa_sample_count(self):
        self.commandline.extend(["--gpu-rasterization-msaa-sample-count"])

    def with_gpu_revision(self):
        self.commandline.extend(["--gpu-revision"])

    def with_gpu_sandbox_allow_sysv_shm(self):
        self.commandline.extend(["--gpu-sandbox-allow-sysv-shm"])

    def with_gpu_sandbox_failures_fatal(self):
        self.commandline.extend(["--gpu-sandbox-failures-fatal"])

    def with_gpu_sandbox_start_early(self):
        self.commandline.extend(["--gpu-sandbox-start-early"])

    def with_gpu_startup_dialog(self):
        self.commandline.extend(["--gpu-startup-dialog"])

    def with_gpu_sub_system_id(self):
        self.commandline.extend(["--gpu-sub-system-id"])

    def with_gpu_vendor_id(self):
        self.commandline.extend(["--gpu-vendor-id"])

    def with_gpu_watchdog_timeout_seconds(self):
        self.commandline.extend(["--gpu-watchdog-timeout-seconds"])

    def with_gpu2_startup_dialog(self):
        self.commandline.extend(["--gpu2-startup-dialog"])

    def with_graphics_buffer_count(self):
        self.commandline.extend(["--graphics-buffer-count"])

    def with_growth_campaigns_path(self):
        self.commandline.extend(["--growth-campaigns-path"])

    def with_guest(self):
        self.commandline.extend(["--guest"])

    def with_guest_wallpaper_large(self):
        self.commandline.extend(["--guest-wallpaper-large"])

    def with_guest_wallpaper_small(self):
        self.commandline.extend(["--guest-wallpaper-small"])

    def with_hardware_video_decode_framerate(self):
        self.commandline.extend(["--hardware-video-decode-framerate"])

    def with_hardware_video_decoding(self):
        self.commandline.extend(["--hardware-video-decoding"])

    def with_hardware_video_encoding(self):
        self.commandline.extend(["--hardware-video-encoding"])

    def with_has_chromeos_keyboard(self):
        self.commandline.extend(["--has-chromeos-keyboard"])

    def with_has_hps(self):
        self.commandline.extend(["--has-hps"])

    def with_has_internal_stylus(self):
        self.commandline.extend(["--has-internal-stylus"])

    def with_has_number_pad(self):
        self.commandline.extend(["--has-number-pad"])

    def with_headless(self):
        self.commandline.extend(["--headless"])

    def with_help(self):
        self.commandline.extend(["--help"])

    def with_hermes_fake(self):
        self.commandline.extend(["--hermes-fake"])

    def with_hidden_network_migration_age(self):
        self.commandline.extend(["--hidden-network-migration-age"])

    def with_hidden_network_migration_interval(self):
        self.commandline.extend(["--hidden-network-migration-interval"])

    def with_hide_crash_restore_bubble(self):
        self.commandline.extend(["--hide-crash-restore-bubble"])

    def with_hide_icons(self):
        self.commandline.extend(["--hide-icons"])

    def with_hide_scrollbars(self):
        self.commandline.extend(["--hide-scrollbars"])

    def with_highlight_all_webviews(self):
        self.commandline.extend(["--highlight-all-webviews"])

    def with_highlight_non_lcd_text_layers(self):
        self.commandline.extend(["--highlight-non-lcd-text-layers"])

    def with_homedir(self):
        self.commandline.extend(["--homedir"])

    def with_homepage(self):
        self.commandline.extend(["--homepage"])

    def with_host(self):
        self.commandline.extend(["--host"])

    def with_host_package_label(self):
        self.commandline.extend(["--host-package-label"])

    def with_host_package_name(self):
        self.commandline.extend(["--host-package-name"])

    def with_host_resolver_rules(self):
        self.commandline.extend(["--host-resolver-rules"])

    def with_host_version_code(self):
        self.commandline.extend(["--host-version-code"])

    def with_icon_reader(self):
        self.commandline.extend(["--icon-reader"])

    def with_ignore_arcvm_dev_conf(self):
        self.commandline.extend(["--ignore-arcvm-dev-conf"])

    def with_ignore_autocomplete_off_autofill(self):
        self.commandline.extend(["--ignore-autocomplete-off-autofill"])

    def with_ignore_certificate_errors_spki_list(self):
        self.commandline.extend(["--ignore-certificate-errors-spki-list"])

    def with_ignore_google_port_numbers(self):
        self.commandline.extend(["--ignore-google-port-numbers"])

    def with_ignore_gpu_blocklist(self):
        self.commandline.extend(["--ignore-gpu-blocklist"])

    def with_ignore_unknown_auth_factors(self):
        self.commandline.extend(["--ignore-unknown-auth-factors"])

    def with_ignore_user_profile_mapping_for_tests(self):
        self.commandline.extend(["--ignore-user-profile-mapping-for-tests"])

    def with_ime(self):
        self.commandline.extend(["--ime"])

    def with_in_process_broker(self):
        self.commandline.extend(["--in-process-broker"])

    def with_in_process_gpu(self):
        self.commandline.extend(["--in-process-gpu"])

    def with_incognito(self):
        self.commandline.extend(["--incognito"])

    def with_init_isolate_as_foreground(self):
        self.commandline.extend(["--init-isolate-as-foreground"])

    def with_initial_preferences_file(self):
        self.commandline.extend(["--initial-preferences-file"])

    def with_initialize_client_hints_storage(self):
        self.commandline.extend(["--initialize-client-hints-storage"])

    def with_input(self):
        self.commandline.extend(["--input"])

    def with_inspector_protocol_log(self):
        self.commandline.extend(["--inspector-protocol-log"])

    def with_install_autogenerated_theme(self):
        self.commandline.extend(["--install-autogenerated-theme"])

    def with_install_chrome_app(self):
        self.commandline.extend(["--install-chrome-app"])

    def with_install_isolated_web_app_from_file(self):
        self.commandline.extend(["--install-isolated-web-app-from-file"])

    def with_install_isolated_web_app_from_url(self):
        self.commandline.extend(["--install-isolated-web-app-from-url"])

    def with_install_log_fast_upload_for_tests(self):
        self.commandline.extend(["--install-log-fast-upload-for-tests"])

    def with_instant_process(self):
        self.commandline.extend(["--instant-process"])

    def with_ip_address_space_overrides(self):
        self.commandline.extend(["--ip-address-space-overrides"])

    def with_ipc_connection_timeout(self):
        self.commandline.extend(["--ipc-connection-timeout"])

    def with_ipc_dump_directory(self):
        self.commandline.extend(["--ipc-dump-directory"])

    def with_ipc_fuzzer_testcase(self):
        self.commandline.extend(["--ipc-fuzzer-testcase"])

    def with_isolate_origins(self):
        self.commandline.extend(["--isolate-origins"])

    def with_isolated_context_origins(self):
        self.commandline.extend(["--isolated-context-origins"])

    def with_isolation_by_default(self):
        self.commandline.extend(["--isolation-by-default"])

    def with_javascript_harmony(self):
        self.commandline.extend(["--javascript-harmony"])

    def with_js_flags(self):
        self.commandline.extend(["--js-flags"])

    def with_keep_alive_for_test(self):
        self.commandline.extend(["--keep-alive-for-test"])

    def with_kiosk(self):
        self.commandline.extend(["--kiosk"])

    def with_kiosk_printing(self):
        self.commandline.extend(["--kiosk-printing"])

    def with_kiosk_splash_screen_min_time_seconds(self):
        self.commandline.extend(["--kiosk-splash-screen-min-time-seconds"])

    def with_lacros_availability_ignore(self):
        self.commandline.extend(["--lacros-availability-ignore"])

    def with_lacros_chrome_additional_args(self):
        self.commandline.extend(["--lacros-chrome-additional-args"])

    def with_lacros_chrome_additional_args_file(self):
        self.commandline.extend(["--lacros-chrome-additional-args-file"])

    def with_lacros_chrome_additional_env(self):
        self.commandline.extend(["--lacros-chrome-additional-env"])

    def with_lacros_chrome_path(self):
        self.commandline.extend(["--lacros-chrome-path"])

    def with_lacros_mojo_socket_for_testing(self):
        self.commandline.extend(["--lacros-mojo-socket-for-testing"])

    def with_lacros_selection_policy_ignore(self):
        self.commandline.extend(["--lacros-selection-policy-ignore"])

    def with_lang(self):
        self.commandline.extend(["--lang"])

    def with_last_launched_app(self):
        self.commandline.extend(["--last-launched-app"])

    def with_launch_rma(self):
        self.commandline.extend(["--launch-rma"])

    def with_launch_time_ticks(self):
        self.commandline.extend(["--launch-time-ticks"])

    def with_layer(self):
        self.commandline.extend(["--layer"])

    def with_libassistant(self):
        self.commandline.extend(["--libassistant"])

    def with_list_apps(self):
        self.commandline.extend(["--list-apps"])

    def with_list_audio_devices(self):
        self.commandline.extend(["--list-audio-devices"])

    def with_llvm_profile_file(self):
        self.commandline.extend(["--llvm-profile-file"])

    def with_load_and_launch_app(self):
        self.commandline.extend(["--load-and-launch-app"])

    def with_load_apps(self):
        self.commandline.extend(["--load-apps"])

    def with_load_extension(self):
        self.commandline.extend(["--load-extension"])

    def with_load_guest_mode_test_extension(self):
        self.commandline.extend(["--load-guest-mode-test-extension"])

    def with_load_signin_profile_test_extension(self):
        self.commandline.extend(["--load-signin-profile-test-extension"])

    def with_loading_predictor_allow_local_request_for_testing(self):
        self.commandline.extend(["--loading-predictor-allow-local-request-for-testing"])

    def with_localhost(self):
        self.commandline.extend(["--localhost"])

    def with_log_best_effort_tasks(self):
        self.commandline.extend(["--log-best-effort-tasks"])

    def with_log_file(self):
        self.commandline.extend(["--log-file"])

    def with_log_gpu_control_list_decisions(self):
        self.commandline.extend(["--log-gpu-control-list-decisions"])

    def with_log_level(self):
        self.commandline.extend(["--log-level"])

    def with_log_missing_unload_ack(self):
        self.commandline.extend(["--log-missing-unload-ack"])

    def with_log_net_log(self):
        self.commandline.extend(["--log-net-log"])

    def with_log_on_ui_double_background_blur(self):
        self.commandline.extend(["--log-on-ui-double-background-blur"])

    def with_login_manager(self):
        self.commandline.extend(["--login-manager"])

    def with_login_profile(self):
        self.commandline.extend(["--login-profile"])

    def with_login_user(self):
        self.commandline.extend(["--login-user"])

    def with_lso_url(self):
        self.commandline.extend(["--lso-url"])

    def with_ltr(self):
        self.commandline.extend(["--ltr"])

    def with_mahi_feature_key(self):
        self.commandline.extend(["--mahi-feature-key"])

    def with_make_chrome_default(self):
        self.commandline.extend(["--make-chrome-default"])

    def with_make_default_browser(self):
        self.commandline.extend(["--make-default-browser"])

    def with_managed_mode(self):
        self.commandline.extend(["--managed-mode"])

    def with_managed_user_id(self):
        self.commandline.extend(["--managed-user-id"])

    def with_mangle_localized_strings(self):
        self.commandline.extend(["--mangle-localized-strings"])

    def with_manual(self):
        self.commandline.extend(["--manual"])

    def with_market_url_for_testing(self):
        self.commandline.extend(["--market-url-for-testing"])

    def with_marketing_opt_in_url(self):
        self.commandline.extend(["--marketing-opt-in-url"])

    def with_max_active_webgl_contexts(self):
        self.commandline.extend(["--max-active-webgl-contexts"])

    def with_max_decoded_image_size_mb(self):
        self.commandline.extend(["--max-decoded-image-size-mb"])

    def with_max_gum_fps(self):
        self.commandline.extend(["--max-gum-fps"])

    def with_max_output_volume_dba1m(self):
        self.commandline.extend(["--max-output-volume-dba1m"])

    def with_max_untiled_layer_height(self):
        self.commandline.extend(["--max-untiled-layer-height"])

    def with_max_untiled_layer_width(self):
        self.commandline.extend(["--max-untiled-layer-width"])

    def with_max_web_media_player_count(self):
        self.commandline.extend(["--max-web-media-player-count"])

    def with_mem_pressure_system_reserved_kb(self):
        self.commandline.extend(["--mem-pressure-system-reserved-kb"])

    def with_memlog(self):
        self.commandline.extend(["--memlog"])

    def with_memlog_sampling_rate(self):
        self.commandline.extend(["--memlog-sampling-rate"])

    def with_memlog_stack_mode(self):
        self.commandline.extend(["--memlog-stack-mode"])

    def with_message_loop_type_ui(self):
        self.commandline.extend(["--message-loop-type-ui"])

    def with_metal(self):
        self.commandline.extend(["--metal"])

    def with_metal_null(self):
        self.commandline.extend(["--metal-null"])

    def with_metrics_client_id(self):
        self.commandline.extend(["--metrics-client-id"])

    def with_metrics_recording_only(self):
        self.commandline.extend(["--metrics-recording-only"])

    def with_metrics_shmem_handle(self):
        self.commandline.extend(["--metrics-shmem-handle"])

    def with_metrics_upload_interval(self):
        self.commandline.extend(["--metrics-upload-interval"])

    def with_mf_cdm(self):
        self.commandline.extend(["--mf-cdm"])

    def with_min_height_for_gpu_raster_tile(self):
        self.commandline.extend(["--min-height-for-gpu-raster-tile"])

    def with_min_video_decoder_output_buffer_size(self):
        self.commandline.extend(["--min-video-decoder-output-buffer-size"])

    def with_minimal(self):
        self.commandline.extend(["--minimal"])

    def with_mirroring(self):
        self.commandline.extend(["--mirroring"])

    def with_mixed(self):
        self.commandline.extend(["--mixed"])

    def with_mixer_enable_dynamic_channel_count(self):
        self.commandline.extend(["--mixer-enable-dynamic-channel-count"])

    def with_mixer_service_endpoint(self):
        self.commandline.extend(["--mixer-service-endpoint"])

    def with_mixer_service_port(self):
        self.commandline.extend(["--mixer-service-port"])

    def with_mixer_source_audio_ready_threshold_ms(self):
        self.commandline.extend(["--mixer-source-audio-ready-threshold-ms"])

    def with_mixer_source_input_queue_ms(self):
        self.commandline.extend(["--mixer-source-input-queue-ms"])

    def with_mock_cert_verifier_default_result_for_testing(self):
        self.commandline.extend(["--mock-cert-verifier-default-result-for-testing"])

    def with_model_quality_service_api_key(self):
        self.commandline.extend(["--model-quality-service-api-key"])

    def with_model_quality_service_url(self):
        self.commandline.extend(["--model-quality-service-url"])

    def with_modifier_split_feature_key(self):
        self.commandline.extend(["--modifier-split-feature-key"])

    def with_mojo_core_library_path(self):
        self.commandline.extend(["--mojo-core-library-path"])

    def with_mojo_is_broker(self):
        self.commandline.extend(["--mojo-is-broker"])

    def with_mojo_local_storage(self):
        self.commandline.extend(["--mojo-local-storage"])

    def with_monitoring_destination_id(self):
        self.commandline.extend(["--monitoring-destination-id"])

    def with_mse_audio_buffer_size_limit_mb(self):
        self.commandline.extend(["--mse-audio-buffer-size-limit-mb"])

    def with_mse_video_buffer_size_limit_mb(self):
        self.commandline.extend(["--mse-video-buffer-size-limit-mb"])

    def with_mute_audio(self):
        self.commandline.extend(["--mute-audio"])

    def with_nacl_debug_mask(self):
        self.commandline.extend(["--nacl-debug-mask"])

    def with_nacl_gdb(self):
        self.commandline.extend(["--nacl-gdb"])

    def with_nacl_gdb_script(self):
        self.commandline.extend(["--nacl-gdb-script"])

    def with_native_messaging_connect_extension(self):
        self.commandline.extend(["--native-messaging-connect-extension"])

    def with_native_messaging_connect_host(self):
        self.commandline.extend(["--native-messaging-connect-host"])

    def with_native_messaging_connect_id(self):
        self.commandline.extend(["--native-messaging-connect-id"])

    def with_nearby_share_certificate_validity_period_hours(self):
        self.commandline.extend(["--nearby-share-certificate-validity-period-hours"])

    def with_nearby_share_device_id(self):
        self.commandline.extend(["--nearby-share-device-id"])

    def with_nearby_share_num_private_certificates(self):
        self.commandline.extend(["--nearby-share-num-private-certificates"])

    def with_nearby_share_verbose_logging(self):
        self.commandline.extend(["--nearby-share-verbose-logging"])

    def with_nearbysharing_http_host(self):
        self.commandline.extend(["--nearbysharing-http-host"])

    def with_net_log_capture_mode(self):
        self.commandline.extend(["--net-log-capture-mode"])

    def with_net_log_max_size_mb(self):
        self.commandline.extend(["--net-log-max-size-mb"])

    def with_netifs_to_ignore(self):
        self.commandline.extend(["--netifs-to-ignore"])

    def with_network_quiet_timeout(self):
        self.commandline.extend(["--network-quiet-timeout"])

    def with_new_window(self):
        self.commandline.extend(["--new-window"])

    def with_no_default_browser_check(self):
        self.commandline.extend(["--no-default-browser-check"])

    def with_no_delay_for_dx12_vulkan_info_collection(self):
        self.commandline.extend(["--no-delay-for-dx12-vulkan-info-collection"])

    def with_no_experiments(self):
        self.commandline.extend(["--no-experiments"])

    def with_no_first_run(self):
        self.commandline.extend(["--no-first-run"])

    def with_no_mojo(self):
        self.commandline.extend(["--no-mojo"])

    def with_no_network_profile_warning(self):
        self.commandline.extend(["--no-network-profile-warning"])

    def with_no_pdf_header_footer(self):
        self.commandline.extend(["--no-pdf-header-footer"])

    def with_no_pings(self):
        self.commandline.extend(["--no-pings"])

    def with_no_pre_read_main_dll(self):
        self.commandline.extend(["--no-pre-read-main-dll"])

    def with_no_proxy_server(self):
        self.commandline.extend(["--no-proxy-server"])

    def with_no_sandbox(self):
        self.commandline.extend(["--no-sandbox"])

    def with_no_service_autorun(self):
        self.commandline.extend(["--no-service-autorun"])

    def with_no_startup_window(self):
        self.commandline.extend(["--no-startup-window"])

    def with_no_system_proxy_config_service(self):
        self.commandline.extend(["--no-system-proxy-config-service"])

    def with_no_unsandboxed_zygote(self):
        self.commandline.extend(["--no-unsandboxed-zygote"])

    def with_no_user_gesture_required(self):
        self.commandline.extend(["--no-user-gesture-required"])

    def with_no_xr_runtime(self):
        self.commandline.extend(["--no-xr-runtime"])

    def with_no_xshm(self):
        self.commandline.extend(["--no-xshm"])

    def with_no_zygote(self):
        self.commandline.extend(["--no-zygote"])

    def with_no_zygote_sandbox(self):
        self.commandline.extend(["--no-zygote-sandbox"])

    def with_noerrdialogs(self):
        self.commandline.extend(["--noerrdialogs"])

    def with_note_taking_app_ids(self):
        self.commandline.extend(["--note-taking-app-ids"])

    def with_notification_inline_reply(self):
        self.commandline.extend(["--notification-inline-reply"])

    def with_notification_launch_id(self):
        self.commandline.extend(["--notification-launch-id"])

    def with_num_raster_threads(self):
        self.commandline.extend(["--num-raster-threads"])

    def with_nv12(self):
        self.commandline.extend(["--nv12"])

    def with_oauth_account_manager_url(self):
        self.commandline.extend(["--oauth-account-manager-url"])

    def with_oauth2_client_id(self):
        self.commandline.extend(["--oauth2-client-id"])

    def with_oauth2_client_secret(self):
        self.commandline.extend(["--oauth2-client-secret"])

    def with_offer_in_settings(self):
        self.commandline.extend(["--offer-in-settings"])

    def with_offscreen_document_testing(self):
        self.commandline.extend(["--offscreen-document-testing"])

    def with_on_the_fly_mhtml_hash_computation(self):
        self.commandline.extend(["--on-the-fly-mhtml-hash-computation"])

    def with_ondevice_validation_request_override(self):
        self.commandline.extend(["--ondevice-validation-request-override"])

    def with_ondevice_validation_write_to_file(self):
        self.commandline.extend(["--ondevice-validation-write-to-file"])

    def with_ondevice_handwriting(self):
        self.commandline.extend(["--ondevice-handwriting"])

    def with_on_device_model_execution(self):
        self.commandline.extend(["--on-device-model-execution"])

    def with_oobe_eula_url_for_tests(self):
        self.commandline.extend(["--oobe-eula-url-for-tests"])

    def with_oobe_force_tablet_first_run(self):
        self.commandline.extend(["--oobe-force-tablet-first-run"])

    def with_oobe_large_screen_special_scaling(self):
        self.commandline.extend(["--oobe-large-screen-special-scaling"])

    def with_oobe_print_frontend_load_timings(self):
        self.commandline.extend(["--oobe-print-frontend-load-timings"])

    def with_oobe_screenshot_dir(self):
        self.commandline.extend(["--oobe-screenshot-dir"])

    def with_oobe_show_accessibility_button_on_marketing_opt_in_for_testing(self):
        self.commandline.extend(
            ["--oobe-show-accessibility-button-on-marketing-opt-in-for-testing"]
        )

    def with_oobe_skip_postlogin(self):
        self.commandline.extend(["--oobe-skip-postlogin"])

    def with_oobe_skip_to_login(self):
        self.commandline.extend(["--oobe-skip-to-login"])

    def with_oobe_timer_interval(self):
        self.commandline.extend(["--oobe-timer-interval"])

    def with_oobe_timezone_override_for_tests(self):
        self.commandline.extend(["--oobe-timezone-override-for-tests"])

    def with_oobe_trigger_sync_timeout_for_tests(self):
        self.commandline.extend(["--oobe-trigger-sync-timeout-for-tests"])

    def with_opengraph(self):
        self.commandline.extend(["--opengraph"])

    def with_openxr(self):
        self.commandline.extend(["--openxr"])

    def with_optimization_guide_fetch_hints_override(self):
        self.commandline.extend(["--optimization-guide-fetch-hints-override"])

    def with_optimization_guide_fetch_hints_override_timer(self):
        self.commandline.extend(["--optimization-guide-fetch-hints-override-timer"])

    def with_optimization_guide_model_execution_validate(self):
        self.commandline.extend(["--optimization-guide-model-execution-validate"])

    def with_optimization_guide_model_override(self):
        self.commandline.extend(["--optimization-guide-model-override"])

    def with_optimization_guide_model_validate(self):
        self.commandline.extend(["--optimization-guide-model-validate"])

    def with_optimization_guide_ondevice_model_execution_override(self):
        self.commandline.extend(
            ["--optimization-guide-ondevice-model-execution-override"]
        )

    def with_optimization_guide_service_api_key(self):
        self.commandline.extend(["--optimization-guide-service-api-key"])

    def with_optimization_guide_service_get_hints_url(self):
        self.commandline.extend(["--optimization-guide-service-get-hints-url"])

    def with_optimization_guide_service_get_models_url(self):
        self.commandline.extend(["--optimization-guide-service-get-models-url"])

    def with_optimization_guide_service_model_execution_url(self):
        self.commandline.extend(["--optimization-guide-service-model-execution-url"])

    def with_optimization_guide_hints_override(self):
        self.commandline.extend(["--optimization-guide-hints-override"])

    def with_orientation_sensors(self):
        self.commandline.extend(["--orientation-sensors"])

    def with_origin_trial_disabled_features(self):
        self.commandline.extend(["--origin-trial-disabled-features"])

    def with_origin_trial_disabled_tokens(self):
        self.commandline.extend(["--origin-trial-disabled-tokens"])

    def with_origin_trial_public_key(self):
        self.commandline.extend(["--origin-trial-public-key"])

    def with_override_enabled_cdm_interface_version(self):
        self.commandline.extend(["--override-enabled-cdm-interface-version"])

    def with_override_hardware_secure_codecs_for_testing(self):
        self.commandline.extend(["--override-hardware-secure-codecs-for-testing"])

    def with_override_language_detection(self):
        self.commandline.extend(["--override-language-detection"])

    def with_override_metrics_upload_url(self):
        self.commandline.extend(["--override-metrics-upload-url"])

    def with_override_use_software_gl_for_tests(self):
        self.commandline.extend(["--override-use-software-gl-for-tests"])

    def with_overview_button_for_tests(self):
        self.commandline.extend(["--overview-button-for-tests"])

    def with_ozone_dump_file(self):
        self.commandline.extend(["--ozone-dump-file"])

    def with_ozone_override_screen_size(self):
        self.commandline.extend(["--ozone-override-screen-size"])

    def with_ozone_platform(self):
        self.commandline.extend(["--ozone-platform"])

    def with_ozone_platform_hint(self):
        self.commandline.extend(["--ozone-platform-hint"])

    def with_pack_extension(self):
        self.commandline.extend(["--pack-extension"])

    def with_pack_extension_key(self):
        self.commandline.extend(["--pack-extension-key"])

    def with_page_content_annotations_validation_batch_size(self):
        self.commandline.extend(["--page-content-annotations-validation-batch-size"])

    def with_page_content_annotations_validation_content_visibility(self):
        self.commandline.extend(
            ["--page-content-annotations-validation-content-visibility"]
        )

    def with_page_content_annotations_validation_startup_delay_seconds(self):
        self.commandline.extend(
            ["--page-content-annotations-validation-startup-delay-seconds"]
        )

    def with_page_content_annotations_validation_write_to_file(self):
        self.commandline.extend(["--page-content-annotations-validation-write-to-file"])

    def with_parent_window(self):
        self.commandline.extend(["--parent-window"])

    def with_passthrough(self):
        self.commandline.extend(["--passthrough"])

    def with_password_store(self):
        self.commandline.extend(["--password-store"])

    def with_pdf_renderer(self):
        self.commandline.extend(["--pdf-renderer"])

    def with_pdf_conversion(self):
        self.commandline.extend(["--pdf-conversion"])

    def with_pen_devices(self):
        self.commandline.extend(["--pen-devices"])

    def with_perf_test_print_uma_means(self):
        self.commandline.extend(["--perf-test-print-uma-means"])

    def with_perfetto_disable_interning(self):
        self.commandline.extend(["--perfetto-disable-interning"])

    def with_performance(self):
        self.commandline.extend(["--performance"])

    def with_picker_feature_key(self):
        self.commandline.extend(["--picker-feature-key"])

    def with_playready_key_system(self):
        self.commandline.extend(["--playready-key-system"])

    def with_policy(self):
        self.commandline.extend(["--policy"])

    def with_policy_verification_key(self):
        self.commandline.extend(["--policy-verification-key"])

    def with_ppapi(self):
        self.commandline.extend(["--ppapi"])

    def with_ppapi_antialiased_text_enabled(self):
        self.commandline.extend(["--ppapi-antialiased-text-enabled"])

    def with_ppapi_in_process(self):
        self.commandline.extend(["--ppapi-in-process"])

    def with_ppapi_plugin_launcher(self):
        self.commandline.extend(["--ppapi-plugin-launcher"])

    def with_ppapi_startup_dialog(self):
        self.commandline.extend(["--ppapi-startup-dialog"])

    def with_ppapi_subpixel_rendering_setting(self):
        self.commandline.extend(["--ppapi-subpixel-rendering-setting"])

    def with_pre_crashpad_crash_test(self):
        self.commandline.extend(["--pre-crashpad-crash-test"])

    def with_prediction_service_mock_likelihood(self):
        self.commandline.extend(["--prediction-service-mock-likelihood"])

    def with_preinstalled_web_apps_dir(self):
        self.commandline.extend(["--preinstalled-web-apps-dir"])

    def with_prevent_kiosk_autolaunch_for_testing(self):
        self.commandline.extend(["--prevent-kiosk-autolaunch-for-testing"])

    def with_prevent_resizing_contents_for_testing(self):
        self.commandline.extend(["--prevent-resizing-contents-for-testing"])

    def with_previous_app(self):
        self.commandline.extend(["--previous-app"])

    def with_print_to_pdf(self):
        self.commandline.extend(["--print-to-pdf"])

    def with_printing_ppd_channel(self):
        self.commandline.extend(["--printing-ppd-channel"])

    def with_privacy_policy_host_for_tests(self):
        self.commandline.extend(["--privacy-policy-host-for-tests"])

    def with_private_aggregation_developer_mode(self):
        self.commandline.extend(["--private-aggregation-developer-mode"])

    def with_privet_ipv6_only(self):
        self.commandline.extend(["--privet-ipv6-only"])

    def with_process_per_site(self):
        self.commandline.extend(["--process-per-site"])

    def with_process_per_tab(self):
        self.commandline.extend(["--process-per-tab"])

    def with_product_version(self):
        self.commandline.extend(["--product-version"])

    def with_production(self):
        self.commandline.extend(["--production"])

    def with_profile_base_name(self):
        self.commandline.extend(["--profile-base-name"])

    def with_profile_directory(self):
        self.commandline.extend(["--profile-directory"])

    def with_profile_email(self):
        self.commandline.extend(["--profile-email"])

    def with_profile_management_attributes(self):
        self.commandline.extend(["--profile-management-attributes"])

    def with_profile_requires_policy(self):
        self.commandline.extend(["--profile-requires-policy"])

    def with_profiling_at_start(self):
        self.commandline.extend(["--profiling-at-start"])

    def with_profiling_file(self):
        self.commandline.extend(["--profiling-file"])

    def with_profiling_flush(self):
        self.commandline.extend(["--profiling-flush"])

    def with_protected_audiences_consented_debug_token(self):
        self.commandline.extend(["--protected-audiences-consented-debug-token"])

    def with_proxy_auto_detect(self):
        self.commandline.extend(["--proxy-auto-detect"])

    def with_proxy_bypass_list(self):
        self.commandline.extend(["--proxy-bypass-list"])

    def with_proxy_pac_url(self):
        self.commandline.extend(["--proxy-pac-url"])

    def with_proxy_server(self):
        self.commandline.extend(["--proxy-server"])

    def with_proxy_resolver_win(self):
        self.commandline.extend(["--proxy-resolver-win"])

    def with_public_accounts_saml_acl_url(self):
        self.commandline.extend(["--public-accounts-saml-acl-url"])

    def with_pull_to_refresh(self):
        self.commandline.extend(["--pull-to-refresh"])

    def with_purge_model_and_features_store(self):
        self.commandline.extend(["--purge-model-and-features-store"])

    def with_purge_optimization_guide_store(self):
        self.commandline.extend(["--purge-optimization-guide-store"])

    def with_pwa_launcher_version(self):
        self.commandline.extend(["--pwa-launcher-version"])

    def with_qs_add_fake_bluetooth_devices(self):
        self.commandline.extend(["--qs-add-fake-bluetooth-devices"])

    def with_qs_add_fake_cast_devices(self):
        self.commandline.extend(["--qs-add-fake-cast-devices"])

    def with_qs_show_locale_tile(self):
        self.commandline.extend(["--qs-show-locale-tile"])

    def with_query_tiles_country_code(self):
        self.commandline.extend(["--query-tiles-country-code"])

    def with_query_tiles_enable_trending(self):
        self.commandline.extend(["--query-tiles-enable-trending"])

    def with_query_tiles_instant_background_task(self):
        self.commandline.extend(["--query-tiles-instant-background-task"])

    def with_query_tiles_rank_tiles(self):
        self.commandline.extend(["--query-tiles-rank-tiles"])

    def with_query_tiles_single_tier(self):
        self.commandline.extend(["--query-tiles-single-tier"])

    def with_quota_change_event_interval(self):
        self.commandline.extend(["--quota-change-event-interval"])

    def with_raise_timer_frequency(self):
        self.commandline.extend(["--raise-timer-frequency"])

    def with_rdp_desktop_session(self):
        self.commandline.extend(["--rdp-desktop-session"])

    def with_reader_mode_feedback(self):
        self.commandline.extend(["--reader-mode-feedback"])

    def with_reader_mode_heuristics(self):
        self.commandline.extend(["--reader-mode-heuristics"])

    def with_realtime_reporting_url(self):
        self.commandline.extend(["--realtime-reporting-url"])

    def with_redirect_libassistant_logging(self):
        self.commandline.extend(["--redirect-libassistant-logging"])

    def with_reduce_accept_language(self):
        self.commandline.extend(["--reduce-accept-language"])

    def with_reduce_user_agent_minor_version(self):
        self.commandline.extend(["--reduce-user-agent-minor-version"])

    def with_reduce_user_agent_platform_oscpu(self):
        self.commandline.extend(["--reduce-user-agent-platform-oscpu"])

    def with_register_max_dark_suspend_delay(self):
        self.commandline.extend(["--register-max-dark-suspend-delay"])

    def with_register_pepper_plugins(self):
        self.commandline.extend(["--register-pepper-plugins"])

    def with_regulatory_label_dir(self):
        self.commandline.extend(["--regulatory-label-dir"])

    def with_relauncher(self):
        self.commandline.extend(["--relauncher"])

    def with_remote_allow_origins(self):
        self.commandline.extend(["--remote-allow-origins"])

    def with_remote_debug_mode(self):
        self.commandline.extend(["--remote-debug-mode"])

    def with_remote_debugging_address(self):
        self.commandline.extend(["--remote-debugging-address"])

    def with_remote_debugging_io_pipes(self):
        self.commandline.extend(["--remote-debugging-io-pipes"])

    def with_remote_debugging_pipe(self):
        self.commandline.extend(["--remote-debugging-pipe"])

    def with_remote_debugging_port(self):
        self.commandline.extend(["--remote-debugging-port"])

    def with_remote_debugging_socket_name(self):
        self.commandline.extend(["--remote-debugging-socket-name"])

    def with_remote_debugging_targets(self):
        self.commandline.extend(["--remote-debugging-targets"])

    def with_remote_reboot_command_timeout_in_seconds_for_testing(self):
        self.commandline.extend(
            ["--remote-reboot-command-timeout-in-seconds-for-testing"]
        )

    def with_renderer(self):
        self.commandline.extend(["--renderer"])

    def with_renderer_client_id(self):
        self.commandline.extend(["--renderer-client-id"])

    def with_renderer_cmd_prefix(self):
        self.commandline.extend(["--renderer-cmd-prefix"])

    def with_renderer_process_limit(self):
        self.commandline.extend(["--renderer-process-limit"])

    def with_renderer_sampling(self):
        self.commandline.extend(["--renderer-sampling"])

    def with_renderer_startup_dialog(self):
        self.commandline.extend(["--renderer-startup-dialog"])

    def with_renderer_wait_for_java_debugger(self):
        self.commandline.extend(["--renderer-wait-for-java-debugger"])

    def with_renderpass(self):
        self.commandline.extend(["--renderpass"])

    def with_report_vp9_as_an_unsupported_mime_type(self):
        self.commandline.extend(["--report-vp9-as-an-unsupported-mime-type"])

    def with_request_desktop_sites(self):
        self.commandline.extend(["--request-desktop-sites"])

    def with_require_wlan(self):
        self.commandline.extend(["--require-wlan"])

    def with_reset_browsing_instance_between_tests(self):
        self.commandline.extend(["--reset-browsing-instance-between-tests"])

    def with_reset_variation_state(self):
        self.commandline.extend(["--reset-variation-state"])

    def with_restart(self):
        self.commandline.extend(["--restart"])

    def with_restore_key_on_lock_screen(self):
        self.commandline.extend(["--restore-key-on-lock-screen"])

    def with_restore_last_session(self):
        self.commandline.extend(["--restore-last-session"])

    def with_restrict_gamepad_access(self):
        self.commandline.extend(["--restrict-gamepad-access"])

    def with_reven_branding(self):
        self.commandline.extend(["--reven-branding"])

    def with_rlz_ping_delay(self):
        self.commandline.extend(["--rlz-ping-delay"])

    def with_rma_not_allowed(self):
        self.commandline.extend(["--rma-not-allowed"])

    def with_rtl(self):
        self.commandline.extend(["--rtl"])

    def with_run_all_compositor_stages_before_draw(self):
        self.commandline.extend(["--run-all-compositor-stages-before-draw"])

    def with_run_manual(self):
        self.commandline.extend(["--run-manual"])

    def with_run_web_tests(self):
        self.commandline.extend(["--run-web-tests"])

    def with_safe_mode(self):
        self.commandline.extend(["--safe-mode"])

    def with_safebrowsing_enable_enhanced_protection(self):
        self.commandline.extend(["--safebrowsing-enable-enhanced-protection"])

    def with_safebrowsing_manual_download_blacklist(self):
        self.commandline.extend(["--safebrowsing-manual-download-blacklist"])

    def with_saml_password_change_url(self):
        self.commandline.extend(["--saml-password-change-url"])

    def with_sandbox_ipc(self):
        self.commandline.extend(["--sandbox-ipc"])

    def with_save_page_as_mhtml(self):
        self.commandline.extend(["--save-page-as-mhtml"])

    def with_scheduled_reboot_grace_period_in_seconds_for_testing(self):
        self.commandline.extend(
            ["--scheduled-reboot-grace-period-in-seconds-for-testing"]
        )

    def with_scheduler_boost_urgent(self):
        self.commandline.extend(["--scheduler-boost-urgent"])

    def with_scheduler_configuration(self):
        self.commandline.extend(["--scheduler-configuration"])

    def with_scheduler_configuration_default(self):
        self.commandline.extend(["--scheduler-configuration-default"])

    def with_screen_capture_audio_default_unchecked(self):
        self.commandline.extend(["--screen-capture-audio-default-unchecked"])

    def with_screen_config(self):
        self.commandline.extend(["--screen-config"])

    def with_screenshot(self):
        self.commandline.extend(["--screenshot"])

    def with_screen_ai(self):
        self.commandline.extend(["--screen-ai"])

    def with_seal_key(self):
        self.commandline.extend(["--seal-key"])

    def with_search_engine_choice_country(self):
        self.commandline.extend(["--search-engine-choice-country"])

    def with_search_provider_logo_url(self):
        self.commandline.extend(["--search-provider-logo-url"])

    def with_secondary_display_layout(self):
        self.commandline.extend(["--secondary-display-layout"])

    def with_secure_connect_api_url(self):
        self.commandline.extend(["--secure-connect-api-url"])

    def with_service(self):
        self.commandline.extend(["--service"])

    def with_service_name(self):
        self.commandline.extend(["--service-name"])

    def with_service_request_attachment_name(self):
        self.commandline.extend(["--service-request-attachment-name"])

    def with_service_sandbox_type(self):
        self.commandline.extend(["--service-sandbox-type"])

    def with_service_with_jit(self):
        self.commandline.extend(["--service-with-jit"])

    def with_set_extension_throttle_test_params(self):
        self.commandline.extend(["--set-extension-throttle-test-params"])

    def with_setup(self):
        self.commandline.extend(["--setup"])

    def with_shader_cache_path(self):
        self.commandline.extend(["--shader-cache-path"])

    def with_shared_array_buffer_allowed_origins(self):
        self.commandline.extend(["--shared-array-buffer-allowed-origins"])

    def with_shared_array_buffer_unrestricted_access_allowed(self):
        self.commandline.extend(["--shared-array-buffer-unrestricted-access-allowed"])

    def with_shared_files(self):
        self.commandline.extend(["--shared-files"])

    def with_shelf_hotseat(self):
        self.commandline.extend(["--shelf-hotseat"])

    def with_shill_stub(self):
        self.commandline.extend(["--shill-stub"])

    def with_short_merge_session_timeout_for_test(self):
        self.commandline.extend(["--short-merge-session-timeout-for-test"])

    def with_short_reporting_delay(self):
        self.commandline.extend(["--short-reporting-delay"])

    def with_show_aggregated_damage(self):
        self.commandline.extend(["--show-aggregated-damage"])

    def with_show_autofill_signatures(self):
        self.commandline.extend(["--show-autofill-signatures"])

    def with_show_autofill_type_predictions(self):
        self.commandline.extend(["--show-autofill-type-predictions"])

    def with_show_component_extension_options(self):
        self.commandline.extend(["--show-component-extension-options"])

    def with_show_composited_layer_borders(self):
        self.commandline.extend(["--show-composited-layer-borders"])

    def with_show_dc_layer_debug_borders(self):
        self.commandline.extend(["--show-dc-layer-debug-borders"])

    def with_show_fps_counter(self):
        self.commandline.extend(["--show-fps-counter"])

    def with_show_icons(self):
        self.commandline.extend(["--show-icons"])

    def with_show_layer_animation_bounds(self):
        self.commandline.extend(["--show-layer-animation-bounds"])

    def with_show_layout_shift_regions(self):
        self.commandline.extend(["--show-layout-shift-regions"])

    def with_show_login_dev_overlay(self):
        self.commandline.extend(["--show-login-dev-overlay"])

    def with_show_mac_overlay_borders(self):
        self.commandline.extend(["--show-mac-overlay-borders"])

    def with_show_oobe_dev_overlay(self):
        self.commandline.extend(["--show-oobe-dev-overlay"])

    def with_show_oobe_quick_start_debugger(self):
        self.commandline.extend(["--show-oobe-quick-start-debugger"])

    def with_show_overdraw_feedback(self):
        self.commandline.extend(["--show-overdraw-feedback"])

    def with_show_paint_rects(self):
        self.commandline.extend(["--show-paint-rects"])

    def with_show_property_changed_rects(self):
        self.commandline.extend(["--show-property-changed-rects"])

    def with_show_screenspace_rects(self):
        self.commandline.extend(["--show-screenspace-rects"])

    def with_show_surface_damage_rects(self):
        self.commandline.extend(["--show-surface-damage-rects"])

    def with_show_taps(self):
        self.commandline.extend(["--show-taps"])

    def with_signed_out_ntp_modules(self):
        self.commandline.extend(["--signed-out-ntp-modules"])

    def with_silent_debugger_extension_api(self):
        self.commandline.extend(["--silent-debugger-extension-api"])

    def with_silent_launch(self):
        self.commandline.extend(["--silent-launch"])

    def with_simulate_browsing_data_lifetime(self):
        self.commandline.extend(["--simulate-browsing-data-lifetime"])

    def with_simulate_critical_update(self):
        self.commandline.extend(["--simulate-critical-update"])

    def with_simulate_elevated_recovery(self):
        self.commandline.extend(["--simulate-elevated-recovery"])

    def with_simulate_idle_timeout(self):
        self.commandline.extend(["--simulate-idle-timeout"])

    def with_simulate_outdated(self):
        self.commandline.extend(["--simulate-outdated"])

    def with_simulate_outdated_no_au(self):
        self.commandline.extend(["--simulate-outdated-no-au"])

    def with_simulate_update_error_code(self):
        self.commandline.extend(["--simulate-update-error-code"])

    def with_simulate_update_hresult(self):
        self.commandline.extend(["--simulate-update-hresult"])

    def with_simulate_upgrade(self):
        self.commandline.extend(["--simulate-upgrade"])

    def with_single_process(self):
        self.commandline.extend(["--single-process"])

    def with_site_per_process(self):
        self.commandline.extend(["--site-per-process"])

    def with_skia_font_cache_limit_mb(self):
        self.commandline.extend(["--skia-font-cache-limit-mb"])

    def with_skia_graphite_backend(self):
        self.commandline.extend(["--skia-graphite-backend"])

    def with_skia_resource_cache_limit_mb(self):
        self.commandline.extend(["--skia-resource-cache-limit-mb"])

    def with_skip_force_online_signin_for_testing(self):
        self.commandline.extend(["--skip-force-online-signin-for-testing"])

    def with_skip_local_upm_gms_core_version_check_for_testing(self):
        self.commandline.extend(["--skip-local-upm-gms-core-version-check-for-testing"])

    def with_skip_multidevice_screen(self):
        self.commandline.extend(["--skip-multidevice-screen"])

    def with_skip_reorder_nudge_show_threshold_duration(self):
        self.commandline.extend(["--skip-reorder-nudge-show-threshold-duration"])

    def with_slow_down_compositing_scale_factor(self):
        self.commandline.extend(["--slow-down-compositing-scale-factor"])

    def with_slow_down_raster_scale_factor(self):
        self.commandline.extend(["--slow-down-raster-scale-factor"])

    def with_sms_test_messages(self):
        self.commandline.extend(["--sms-test-messages"])

    def with_source_shortcut(self):
        self.commandline.extend(["--source-shortcut"])

    def with_speech_recognition(self):
        self.commandline.extend(["--speech-recognition"])

    def with_ssl_key_log_file(self):
        self.commandline.extend(["--ssl-key-log-file"])

    def with_ssl_version_max(self):
        self.commandline.extend(["--ssl-version-max"])

    def with_ssl_version_min(self):
        self.commandline.extend(["--ssl-version-min"])

    def with_stabilize_time_dependent_view_for_tests(self):
        self.commandline.extend(["--stabilize-time-dependent-view-for-tests"])

    def with_stable_release_mode(self):
        self.commandline.extend(["--stable-release-mode"])

    def with_staging(self):
        self.commandline.extend(["--staging"])

    def with_start_fullscreen(self):
        self.commandline.extend(["--start-fullscreen"])

    def with_start_maximized(self):
        self.commandline.extend(["--start-maximized"])

    def with_start_stack_profiler(self):
        self.commandline.extend(["--start-stack-profiler"])

    def with_start_stack_profiler_with_java_name_hashing(self):
        self.commandline.extend(["--start-stack-profiler-with-java-name-hashing"])

    def with_suppress_message_center_popups(self):
        self.commandline.extend(["--suppress-message-center-popups"])

    def with_system_aec_enabled(self):
        self.commandline.extend(["--system-aec-enabled"])

    def with_system_developer_mode(self):
        self.commandline.extend(["--system-developer-mode"])

    def with_system_font_family(self):
        self.commandline.extend(["--system-font-family"])

    def with_system_log_upload_frequency(self):
        self.commandline.extend(["--system-log-upload-frequency"])

    def with_test_encryption_migration_ui(self):
        self.commandline.extend(["--test-encryption-migration-ui"])

    def with_test_memory_log_delay_in_minutes(self):
        self.commandline.extend(["--test-memory-log-delay-in-minutes"])

    def with_test_name(self):
        self.commandline.extend(["--test-name"])

    def with_test_register_standard_scheme(self):
        self.commandline.extend(["--test-register-standard-scheme"])

    def with_test_third_party_cookie_phaseout(self):
        self.commandline.extend(["--test-third-party-cookie-phaseout"])

    def with_test_type(self):
        self.commandline.extend(["--test-type"])

    def with_test_wallpaper_server(self):
        self.commandline.extend(["--test-wallpaper-server"])

    def with_tether_host_scans_ignore_wired_connections(self):
        self.commandline.extend(["--tether-host-scans-ignore-wired-connections"])

    def with_tether_stub(self):
        self.commandline.extend(["--tether-stub"])

    def with_time_before_onboarding_survey_in_seconds_for_testing(self):
        self.commandline.extend(
            ["--time-before-onboarding-survey-in-seconds-for-testing"]
        )

    def with_time_ticks_at_unix_epoch(self):
        self.commandline.extend(["--time-ticks-at-unix-epoch"])

    def with_time_zone_for_testing(self):
        self.commandline.extend(["--time-zone-for-testing"])

    def with_timeout(self):
        self.commandline.extend(["--timeout"])

    def with_tls1_2(self):
        self.commandline.extend(["--tls1-2"])

    def with_tls1_3(self):
        self.commandline.extend(["--tls1-3"])

    def with_top_chrome_touch_ui(self):
        self.commandline.extend(["--top-chrome-touch-ui"])

    def with_top_controls_show_threshold(self):
        self.commandline.extend(["--top-controls-show-threshold"])

    def with_touch_events(self):
        self.commandline.extend(["--touch-events"])

    def with_tpm_is_dynamic(self):
        self.commandline.extend(["--tpm-is-dynamic"])

    def with_trace_config_file(self):
        self.commandline.extend(["--trace-config-file"])

    def with_trace_smb_size(self):
        self.commandline.extend(["--trace-smb-size"])

    def with_trace_startup(self):
        self.commandline.extend(["--trace-startup"])

    def with_trace_startup_duration(self):
        self.commandline.extend(["--trace-startup-duration"])

    def with_trace_startup_enable_privacy_filtering(self):
        self.commandline.extend(["--trace-startup-enable-privacy-filtering"])

    def with_trace_startup_file(self):
        self.commandline.extend(["--trace-startup-file"])

    def with_trace_startup_format(self):
        self.commandline.extend(["--trace-startup-format"])

    def with_trace_startup_owner(self):
        self.commandline.extend(["--trace-startup-owner"])

    def with_trace_startup_record_mode(self):
        self.commandline.extend(["--trace-startup-record-mode"])

    def with_trace_to_console(self):
        self.commandline.extend(["--trace-to-console"])

    def with_trace_to_file(self):
        self.commandline.extend(["--trace-to-file"])

    def with_trace_to_file_name(self):
        self.commandline.extend(["--trace-to-file-name"])

    def with_translate_ranker_model_url(self):
        self.commandline.extend(["--translate-ranker-model-url"])

    def with_translate_script_url(self):
        self.commandline.extend(["--translate-script-url"])

    def with_translate_security_origin(self):
        self.commandline.extend(["--translate-security-origin"])

    def with_trusted_download_sources(self):
        self.commandline.extend(["--trusted-download-sources"])

    def with_try_supported_channel_layouts(self):
        self.commandline.extend(["--try-supported-channel-layouts"])

    def with_ui_disable_partial_swap(self):
        self.commandline.extend(["--ui-disable-partial-swap"])

    def with_ui_enable_layer_lists(self):
        self.commandline.extend(["--ui-enable-layer-lists"])

    def with_ui_toolkit(self):
        self.commandline.extend(["--ui-toolkit"])

    def with_ukm_server_url(self):
        self.commandline.extend(["--ukm-server-url"])

    def with_uma_insecure_server_url(self):
        self.commandline.extend(["--uma-insecure-server-url"])

    def with_uma_server_url(self):
        self.commandline.extend(["--uma-server-url"])

    def with_unfiltered_bluetooth_devices(self):
        self.commandline.extend(["--unfiltered-bluetooth-devices"])

    def with_uninstall(self):
        self.commandline.extend(["--uninstall"])

    def with_uninstall_app_id(self):
        self.commandline.extend(["--uninstall-app-id"])

    def with_unlimited_storage(self):
        self.commandline.extend(["--unlimited-storage"])

    def with_unsafely_allow_protected_media_identifier_for_domain(self):
        self.commandline.extend(
            ["--unsafely-allow-protected-media-identifier-for-domain"]
        )

    def with_unsafely_treat_insecure_origin_as_secure(self):
        self.commandline.extend(["--unsafely-treat-insecure-origin-as-secure"])

    def with_use_adapter_luid(self):
        self.commandline.extend(["--use-adapter-luid"])

    def with_use_angle(self):
        self.commandline.extend(["--use-angle"])

    def with_use_cast_browser_pref_config(self):
        self.commandline.extend(["--use-cast-browser-pref-config"])

    def with_use_cmd_decoder(self):
        self.commandline.extend(["--use-cmd-decoder"])

    def with_use_cras(self):
        self.commandline.extend(["--use-cras"])

    def with_use_fake_codec_for_peer_connection(self):
        self.commandline.extend(["--use-fake-codec-for-peer-connection"])

    def with_use_fake_cras_audio_client_for_dbus(self):
        self.commandline.extend(["--use-fake-cras-audio-client-for-dbus"])

    def with_use_fake_device_for_media_stream(self):
        self.commandline.extend(["--use-fake-device-for-media-stream"])

    def with_use_fake_mahi_manager(self):
        self.commandline.extend(["--use-fake-mahi-manager"])

    def with_use_fake_mjpeg_decode_accelerator(self):
        self.commandline.extend(["--use-fake-mjpeg-decode-accelerator"])

    def with_use_fake_ui_for_digital_identity(self):
        self.commandline.extend(["--use-fake-ui-for-digital-identity"])

    def with_use_fake_ui_for_fedcm(self):
        self.commandline.extend(["--use-fake-ui-for-fedcm"])

    def with_use_fake_ui_for_media_stream(self):
        self.commandline.extend(["--use-fake-ui-for-media-stream"])

    def with_use_file_for_fake_audio_capture(self):
        self.commandline.extend(["--use-file-for-fake-audio-capture"])

    def with_use_file_for_fake_video_capture(self):
        self.commandline.extend(["--use-file-for-fake-video-capture"])

    def with_use_first_display_as_internal(self):
        self.commandline.extend(["--use-first-display-as-internal"])

    def with_use_first_party_set(self):
        self.commandline.extend(["--use-first-party-set"])

    def with_use_gl(self):
        self.commandline.extend(["--use-gl"])

    def with_use_gpu_high_thread_priority_for_perf_tests(self):
        self.commandline.extend(["--use-gpu-high-thread-priority-for-perf-tests"])

    def with_use_gpu_in_tests(self):
        self.commandline.extend(["--use-gpu-in-tests"])

    def with_use_heap_profiling_proto_writer(self):
        self.commandline.extend(["--use-heap-profiling-proto-writer"])

    def with_use_legacy_metrics_service(self):
        self.commandline.extend(["--use-legacy-metrics-service"])

    def with_use_mobile_user_agent(self):
        self.commandline.extend(["--use-mobile-user-agent"])

    def with_use_mock_cert_verifier_for_testing(self):
        self.commandline.extend(["--use-mock-cert-verifier-for-testing"])

    def with_use_mock_keychain(self):
        self.commandline.extend(["--use-mock-keychain"])

    def with_use_myfiles_in_user_data_dir_for_testing(self):
        self.commandline.extend(["--use-myfiles-in-user-data-dir-for-testing"])

    def with_use_redist_dml(self):
        self.commandline.extend(["--use-redist-dml"])

    def with_use_related_website_set(self):
        self.commandline.extend(["--use-related-website-set"])

    def with_use_system_clipboard(self):
        self.commandline.extend(["--use-system-clipboard"])

    def with_use_system_default_printer(self):
        self.commandline.extend(["--use-system-default-printer"])

    def with_use_system_proxy_resolver(self):
        self.commandline.extend(["--use-system-proxy-resolver"])

    def with_use_va_dev_keys(self):
        self.commandline.extend(["--use-va-dev-keys"])

    def with_use_vulkan(self):
        self.commandline.extend(["--use-vulkan"])

    def with_use_wayland_explicit_grab(self):
        self.commandline.extend(["--use-wayland-explicit-grab"])

    def with_user_agent(self):
        self.commandline.extend(["--user-agent"])

    def with_user_agent_product(self):
        self.commandline.extend(["--user-agent-product"])

    def with_user_data_dir(self):
        self.commandline.extend(["--user-data-dir"])

    def with_user_data_migrated(self):
        self.commandline.extend(["--user-data-migrated"])

    def with_user_gesture_required(self):
        self.commandline.extend(["--user-gesture-required"])

    def with_utility(self):
        self.commandline.extend(["--utility"])

    def with_utility_and_browser(self):
        self.commandline.extend(["--utility-and-browser"])

    def with_utility_cmd_prefix(self):
        self.commandline.extend(["--utility-cmd-prefix"])

    def with_utility_sampling(self):
        self.commandline.extend(["--utility-sampling"])

    def with_utility_startup_dialog(self):
        self.commandline.extend(["--utility-startup-dialog"])

    def with_utility_sub_type(self):
        self.commandline.extend(["--utility-sub-type"])

    def with_v(self):
        self.commandline.extend(["--v"])

    def with_v8_cache_options(self):
        self.commandline.extend(["--v8-cache-options"])

    def with_validate_crx(self):
        self.commandline.extend(["--validate-crx"])

    def with_validate_input_event_stream(self):
        self.commandline.extend(["--validate-input-event-stream"])

    def with_validating(self):
        self.commandline.extend(["--validating"])

    def with_variations_insecure_server_url(self):
        self.commandline.extend(["--variations-insecure-server-url"])

    def with_variations_override_country(self):
        self.commandline.extend(["--variations-override-country"])

    def with_variations_seed_fetch_interval(self):
        self.commandline.extend(["--variations-seed-fetch-interval"])

    def with_variations_seed_version(self):
        self.commandline.extend(["--variations-seed-version"])

    def with_variations_server_url(self):
        self.commandline.extend(["--variations-server-url"])

    def with_variations_test_seed_path(self):
        self.commandline.extend(["--variations-test-seed-path"])

    def with_verbose_logging_in_nacl(self):
        self.commandline.extend(["--verbose-logging-in-nacl"])

    def with_version(self):
        self.commandline.extend(["--version"])

    def with_video_capture_use_gpu_memory_buffer(self):
        self.commandline.extend(["--video-capture-use-gpu-memory-buffer"])

    def with_video_image_texture_target(self):
        self.commandline.extend(["--video-image-texture-target"])

    def with_video_threads(self):
        self.commandline.extend(["--video-threads"])

    def with_view_stack_traces(self):
        self.commandline.extend(["--view-stack-traces"])

    def with_virtual_time_budget(self):
        self.commandline.extend(["--virtual-time-budget"])

    def with_viz_demo_use_gpu(self):
        self.commandline.extend(["--viz-demo-use-gpu"])

    def with_vmodule(self):
        self.commandline.extend(["--vmodule"])

    def with_vsync_interval(self):
        self.commandline.extend(["--vsync-interval"])

    def with_vulkan(self):
        self.commandline.extend(["--vulkan"])

    def with_vulkan_heap_memory_limit_mb(self):
        self.commandline.extend(["--vulkan-heap-memory-limit-mb"])

    def with_vulkan_null(self):
        self.commandline.extend(["--vulkan-null"])

    def with_vulkan_sync_cpu_memory_limit_mb(self):
        self.commandline.extend(["--vulkan-sync-cpu-memory-limit-mb"])

    def with_wait_for_debugger(self):
        self.commandline.extend(["--wait-for-debugger"])

    def with_wait_for_debugger_children(self):
        self.commandline.extend(["--wait-for-debugger-children"])

    def with_wait_for_debugger_on_navigation(self):
        self.commandline.extend(["--wait-for-debugger-on-navigation"])

    def with_wait_for_debugger_webui(self):
        self.commandline.extend(["--wait-for-debugger-webui"])

    def with_wallet_service_use_sandbox(self):
        self.commandline.extend(["--wallet-service-use-sandbox"])

    def with_waveout_buffers(self):
        self.commandline.extend(["--waveout-buffers"])

    def with_web_otp_backend(self):
        self.commandline.extend(["--web-otp-backend"])

    def with_web_otp_backend_auto(self):
        self.commandline.extend(["--web-otp-backend-auto"])

    def with_web_otp_backend_sms_verification(self):
        self.commandline.extend(["--web-otp-backend-sms-verification"])

    def with_web_otp_backend_user_consent(self):
        self.commandline.extend(["--web-otp-backend-user-consent"])

    def with_web_sql_access(self):
        self.commandline.extend(["--web-sql-access"])

    def with_web_ui_data_source_path_for_testing(self):
        self.commandline.extend(["--web-ui-data-source-path-for-testing"])

    def with_webapk_server_url(self):
        self.commandline.extend(["--webapk-server-url"])

    def with_webauthn_permit_enterprise_attestation(self):
        self.commandline.extend(["--webauthn-permit-enterprise-attestation"])

    def with_webauthn_remote_desktop_support(self):
        self.commandline.extend(["--webauthn-remote-desktop-support"])

    def with_webauthn_remote_proxied_requests_allowed_additional_origin(self):
        self.commandline.extend(
            ["--webauthn-remote-proxied-requests-allowed-additional-origin="]
        )

    def with_webgl_antialiasing_mode(self):
        self.commandline.extend(["--webgl-antialiasing-mode"])

    def with_webgl_msaa_sample_count(self):
        self.commandline.extend(["--webgl-msaa-sample-count"])

    def with_webrtc_event_log_proactive_pruning_delta(self):
        self.commandline.extend(["--webrtc-event-log-proactive-pruning-delta"])

    def with_webrtc_event_log_upload_delay_ms(self):
        self.commandline.extend(["--webrtc-event-log-upload-delay-ms"])

    def with_webrtc_event_log_upload_no_suppression(self):
        self.commandline.extend(["--webrtc-event-log-upload-no-suppression"])

    def with_webrtc_event_logging(self):
        self.commandline.extend(["--webrtc-event-logging"])

    def with_webrtc_ip_handling_policy(self):
        self.commandline.extend(["--webrtc-ip-handling-policy"])

    def with_webview_disable_app_recovery(self):
        self.commandline.extend(["--webview-disable-app-recovery"])

    def with_webview_disable_safebrowsing_support(self):
        self.commandline.extend(["--webview-disable-safebrowsing-support"])

    def with_webview_draw_functor_uses_vulkan(self):
        self.commandline.extend(["--webview-draw-functor-uses-vulkan"])

    def with_webview_enable_app_recovery(self):
        self.commandline.extend(["--webview-enable-app-recovery"])

    def with_webview_enable_modern_cookie_same_site(self):
        self.commandline.extend(["--webview-enable-modern-cookie-same-site"])

    def with_webview_enable_trust_tokens_component(self):
        self.commandline.extend(["--webview-enable-trust-tokens-component"])

    def with_webview_fenced_frames(self):
        self.commandline.extend(["--webview-fenced-frames"])

    def with_webview_force_crash_java(self):
        self.commandline.extend(["--webview-force-crash-java"])

    def with_webview_force_crash_native(self):
        self.commandline.extend(["--webview-force-crash-native"])

    def with_webview_force_disable_3pcs(self):
        self.commandline.extend(["--webview-force-disable-3pcs"])

    def with_webview_fps_component(self):
        self.commandline.extend(["--webview-fps-component"])

    def with_webview_log_js_console_messages(self):
        self.commandline.extend(["--webview-log-js-console-messages"])

    def with_webview_safebrowsing_block_all_resources(self):
        self.commandline.extend(["--webview-safebrowsing-block-all-resources"])

    def with_webview_sandboxed_renderer(self):
        self.commandline.extend(["--webview-sandboxed-renderer"])

    def with_webview_selective_image_inversion_darkening(self):
        self.commandline.extend(["--webview-selective-image-inversion-darkening"])

    def with_webview_tpcd_metadata_component(self):
        self.commandline.extend(["--webview-tpcd-metadata-component"])

    def with_webview_verbose_logging(self):
        self.commandline.extend(["--webview-verbose-logging"])

    def with_win_jumplist_action(self):
        self.commandline.extend(["--win-jumplist-action"])

    def with_window_title(self, title):
        self.commandline.extend(["--window-name=%s" % (title)])

    def with_window_position(self, x, y):
        self.commandline.extend(["--window-position=%s,%s" % (x, y)])

    def with_window_size(self, width, height):
        self.commandline.extend(["--window-size=%s,%s" % (width, height)])

    def with_window_workspace(self):
        self.commandline.extend(["--window-workspace"])

    def with_winhttp_proxy_resolver(self):
        self.commandline.extend(["--winhttp-proxy-resolver"])

    def with_wm_window_animations_disabled(self):
        self.commandline.extend(["--wm-window-animations-disabled"])

    def with_xr_compositing(self):
        self.commandline.extend(["--xr_compositing"])

    def with_xsession_chooser(self):
        self.commandline.extend(["--xsession_chooser"])

    def with_yuy2(self):
        self.commandline.extend(["--yuy2"])

    def with_zygote(self):
        self.commandline.extend(["--zygote"])

    def run(self):
        import sys

        chromium_path = (
            find_path()
        )  # Hier rufen wir die Funktion auf, um den Chromium-Pfad zu erhalten
        for item in self.commandline:
            flags = [chromium_path, item]
        try:
            subsystem.Popen(
                flags,
                stdout=subsystem.PIPE,
                stderr=subsystem.PIPE,
                stdin=subsystem.PIPE,
            )
        except KeyboardInterrupt:
            print("Chromium browser not found!")
            sys.exit(1)


app = Interface()
app.with_window_title("Interface")
app.with_app(url="https://example.com")
app.with_window_size(600, 600)

app.run()
