# Chromium_flags

```bash
--accept-empty-variations-seed-signature
--accept-lang
--accept-resource-provider
--adaboost
--add-gpu-appcontainer-caps[1]
--add-xr-appcontainer-caps[1]
--additional-private-state-token-key-commitments
--aggressive-cache-discard
--all
--all-renderers
--allarticles
--allow-command-line-plugins
--allow-cross-origin-auth-prompt
--allow-empty-passwords-in-tests
--allow-external-pages
--allow-failed-policy-fetch-for-test
--allow-file-access-from-files
--allow-future-manifest-version
--allow-http-background-page
--allow-http-screen-capture
--allow-insecure-localhost
--allow-legacy-extension-manifests
--allow-loopback-in-peer-connection
--allow-nacl-crxfs-api[2]
--allow-nacl-file-handle-api[2]
--allow-nacl-socket-api[2]
--allow-os-install
--allow-pre-commit-input
--allow-profiles-outside-user-dir
--allow-ra-in-dev-mode[3]
--allow-running-insecure-content[4]
--allow-sandbox-debugging
--allow-silent-push
--allow-third-party-modules[1]
--allowlisted-extension-id
--almanac-api-url
--alsa-amp-device-name
--alsa-amp-element-name
--alsa-check-close-timeout
--alsa-enable-upsampling
--alsa-fixed-output-sample-rate
--alsa-input-device[5]
--alsa-mute-device-name
--alsa-mute-element-name
--alsa-output-avail-min
--alsa-output-buffer-size
--alsa-output-device[5]
--alsa-output-period-size
--alsa-output-start-threshold
--alsa-volume-device-name
--alsa-volume-element-name
--also-emit-success-logs
--always-enable-hdcp
--always-use-complex-text
--angle
--animated-image-resume
--animation-duration-scale
--app
--app-auto-launched
--app-id
--app-launch-url-for-shortcuts-menu-item
--app-mode-auth-code
--app-mode-oauth-token
--app-mode-oem-manifest
--app-run-on-os-login-mode
--app-shell-allow-roaming[6]
--app-shell-host-window-size[6]
--app-shell-preferred-network[6]
--apps-gallery-download-url
--apps-gallery-update-url
--apps-gallery-url
--apps-keep-chrome-alive-in-tests[7]
--arc-availability
--arc-available
--arc-block-keymint
--arc-data-cleanup-on-start
--arc-disable-app-sync
--arc-disable-dexopt-cache
--arc-disable-download-provider
--arc-disable-gms-core-cache
--arc-disable-locale-sync
--arc-disable-media-store-maintenance
--arc-disable-play-auto-install
--arc-disable-tts-cache
--arc-erofs
--arc-force-mount-android-volumes-in-files
--arc-force-show-optin-ui
--arc-generate-play-auto-install
--arc-host-ureadahead-mode
--arc-install-event-chrome-log-for-tests
--arc-packages-cache-mode
--arc-play-store-auto-update
--arc-scale
--arc-start-mode
--arc-tos-host-for-tests
--arc-use-dev-caches
--arcore
--arcvm-ureadahead-mode
--arcvm-use-hugepages
--as-browser
--ash-allow-default-shelf-pin-layout-ignoring-sync
--ash-bypass-glanceables-pref
--ash-clear-fast-ink-buffer
--ash-constrain-pointer-to-root
--ash-contextual-nudges-interval
--ash-contextual-nudges-reset-shown-count
--ash-debug-shortcuts
--ash-dev-shortcuts
--ash-disable-touch-exploration-mode
--ash-enable-magnifier-key-scroller
--ash-enable-palette-on-all-displays
--ash-enable-software-mirroring
--ash-enable-unified-desktop[6]
--ash-hide-notifications-for-factory
--ash-host-window-bounds
--ash-no-nudges
--ash-power-button-position
--ash-side-volume-button-position
--ash-touch-hud
--attestation-server
--attribution-reporting-debug-mode
--audio
--audio-buffer-size
--audio-capturer-with-echo-cancellation[8]
--audio-codecs-from-edid[9]
--audio-output-channels
--audio-output-sample-rate
--audio-process-high-priority[1]
--aue-reached-for-update-required-test
--aura-legacy-power-button
--auth-server-allowlist
--auth-spnego-account-type[10]
--auto
--auto-accept-camera-and-microphone-capture
--auto-accept-this-tab-capture
--auto-grant-captured-surface-control-prompt
--auto-open-devtools-for-tabs
--auto-reject-this-tab-capture
--auto-select-desktop-capture-source
--auto-select-tab-capture-source-by-title
--auto-select-window-capture-source-by-title
--autofill-api-key
--autofill-server-url
--autofill-upload-throttling-period-in-days
--autoplay-policy
--back-gesture-horizontal-threshold
--background-tracing-output-file
--bgra
--biod-fake
--blink-settings
--block-new-web-contents
--bootstrap
--borealis-launch-options
--bottom-gesture-start-height
--bound-session-cookie-rotation-delay
--bound-session-cookie-rotation-result
--browser
--browser-data-backward-migration-for-user
--browser-data-backward-migration-mode
--browser-data-migration-for-user
--browser-data-migration-mode
--browser-startup-dialog
--browser-subprocess-path
--browser-test
--browser-ui-tests-verify-pixels
--bwsi
--bypass-app-banner-engagement-checks
--bypass-installable-message-throttle-for-testing
--campbell-key
--canvas-2d-layers
--cardboard
--cast-app-background-color
--cast-developer-certificate-path
--cast-initial-screen-height
--cast-initial-screen-width
--cast-log-device-cert-chain
--cast-mirroring-target-playout-delay
--cast-mojo-broker-path
--cast-streaming-force-disable-hardware-h264
--cast-streaming-force-disable-hardware-vp8
--cast-streaming-force-enable-hardware-h264
--cast-streaming-force-enable-hardware-vp8
--cc-layer-tree-test-long-timeout
--cc-layer-tree-test-no-timeout
--cc-scroll-animation-duration-in-seconds
--cdm
--cdm-data-directory
--cdm-data-quota-bytes
--cellular-first
--change-stack-guard-on-fork
--character
--check-accessibility-permission
--check-damage-early
--check-for-update-interval
--check-permission
--check-screen-recording-permission
--child-wallpaper-large
--child-wallpaper-small
--cipher-suite-blacklist
--clamshell
--clear-key-cdm-path-for-testing
--clear-token-service
--compensate-for-unstable-pinch-zoom
--compile-shader-always-succeeds
--component-updater
--component-updater-trust-tokens-component-path
--conditional-focus-window-ms
--connectivity-check-url
--conservative
--container-app-preinstall-key
--content-shell-devtools-tab-target
--content-shell-hide-toolbar
--content-shell-host-window-size
--context-provider
--controller
--coral-feature-key
--cors-exempt-headers
--crash-dumps-dir
--crash-loop-before
--crash-on-failure
--crash-on-hang-threads
--crash-server-url
--crash-test
--crashpad-handler
--crashpad-handler-pid
--create-browser-on-startup-for-tests
--credits
--cros-disks-fake
--cros-postlogin-data-fd
--cros-postlogin-log-file
--cros-region
--cros-startup-data-fd
--crosh-command
--cryptauth-http-host
--cryptauth-v2-devicesync-http-host
--cryptauth-v2-enrollment-http-host
--cryptohome-ignore-cleanup-ownership-for-testing
--cryptohome-recovery-service-base-url
--cryptohome-recovery-use-test-env
--cryptohome-use-authsession
--cryptohome-use-old-encryption-for-testing
--custom-android-messages-domain
--custom-devtools-frontend
--custom_summary
--d3d-support
--d3d11
--d3d11-null
--d3d11on12
--d3d9
--daemon
--dark-mode-settings
--data-path
--data-quota-bytes
--data-url-in-svg-use-enabled
--dawn
--dawn-d3d11
--dawn-d3d12
--dawn-metal
--dawn-swiftshader
--dawn-vulkan
--dbus-stub
--deadline-to-synchronize-surfaces
--debug-devtools
--debug-packed-apps
--debug-print
--default-background-color
--default-country-code
--default-tile-height
--default-tile-width
--default-trace-buffer-size-limit-in-kb
--default-wallpaper-is-oem
--default-wallpaper-large
--default-wallpaper-small
--defer-external-display-timeout
--defer-feature-list
--demo-mode-enrolling-username
--demo-mode-force-arc-offline-provision
--demo-mode-highlights-extension
--demo-mode-screensaver-extension
--demo-mode-swa-content-directory
--deny-permission-prompts
--derelict-detection-timeout
--derelict-idle-timeout
--desktop-window-1080p
--deterministic-mode
--device-management-url
--device-scale-factor
--devtools-code-coverage
--devtools-flags
--diagnostics
--diagnostics-format
--diagnostics-recovery
--direct-composition-video-swap-chain-format
--disable-2d-canvas-clip-aa
--disable-2d-canvas-image-chromium
--disable-3d-apis
--disable-accelerated-2d-canvas
--disable-accelerated-mjpeg-decode
--disable-accelerated-video-decode
--disable-accelerated-video-encode
--disable-adpf
--disable-angle-features
--disable-app-content-verification
--disable-arc-cpu-restriction
--disable-arc-data-wipe
--disable-arc-opt-in-verification
--disable-audio-input
--disable-auto-maximize-for-tests
--disable-auto-reload
--disable-auto-wpt-origin-isolation
--disable-ax-menu-list
--disable-back-forward-cache
--disable-background-media-suspend
--disable-background-networking
--disable-background-timer-throttling
--disable-backgrounding-occluded-windows
--disable-backing-store-limit
--disable-best-effort-tasks
--disable-blink-features
--disable-breakpad
--disable-cancel-all-touches
--disable-canvas-aa
--disable-checker-imaging
--disable-checking-optimization-guide-user-permissions
--disable-chrome-tracing-computation
--disable-component-extensions-with-background-pages
--disable-component-update
--disable-composited-antialiasing
--disable-cookie-encryption
--disable-crash-reporter
--disable-databases
--disable-dawn-features
--disable-default-apps
--disable-demo-mode
--disable-dev-shm-usage
--disable-device-disabling
--disable-dinosaur-easter-egg
--disable-disallow-lacros
--disable-domain-blocking-for-3d-apis
--disable-domain-reliability
--disable-drive-fs-for-testing
--disable-explicit-dma-fences
--disable-extensions
--disable-extensions-except
--disable-extensions-file-access-check
--disable-extensions-http-throttling
--disable-fetching-hints-at-navigation-start
--disable-field-trial-config
--disable-file-system
--disable-fine-grained-time-zone-detection
--disable-first-run-ui
--disable-font-subpixel-positioning
--disable-frame-rate-limit
--disable-gaia-services
--disable-gesture-requirement-for-presentation
--disable-gl-drawing-for-tests
--disable-gl-error-limit
--disable-gl-extensions
--disable-glsl-translator
--disable-gpu
--disable-gpu-compositing
--disable-gpu-driver-bug-workarounds
--disable-gpu-early-init
--disable-gpu-memory-buffer-compositor-resources
--disable-gpu-memory-buffer-video-frames
--disable-gpu-process-crash-limit
--disable-gpu-process-for-dx12-info-collection
--disable-gpu-program-cache
--disable-gpu-rasterization
--disable-gpu-sandbox
--disable-gpu-shader-disk-cache
--disable-gpu-vsync
--disable-gpu-watchdog
--disable-hang-monitor
--disable-headless-mode
--disable-hid-blocklist
--disable-hid-detection-on-oobe
--disable-highres-timer
--disable-histogram-customizer
--disable-image-animation-resync
--disable-in-process-stack-traces
--disable-input-event-activation-protection
--disable-ios-password-suggestions
--disable-ip-privacy-proxy
--disable-ipc-flooding-protection
--disable-javascript-harmony-shipping
--disable-kill-after-bad-ipc
--disable-lacros-keep-alive
--disable-layer-tree-host-memory-pressure
--disable-lazy-loading
--disable-lcd-text
--disable-legacy-window
--disable-libassistant-logfile
--disable-local-storage
--disable-logging
--disable-logging-redirect
--disable-login-animations
--disable-login-lacros-opening
--disable-login-screen-apps
--disable-low-end-device-mode
--disable-low-latency-dxva
--disable-low-res-tiling
--disable-machine-cert-request
--disable-main-frame-before-activation
--disable-media-session-api
--disable-metal-shader-cache
--disable-mipmap-generation
--disable-modal-animations
--disable-model-download-verification
--disable-mojo-broker
--disable-mojo-renderer
--disable-nacl
--disable-namespace-sandbox
--disable-new-base-url-inheritance-behavior
--disable-new-content-rendering-timeout
--disable-notifications
--disable-nv12-dxgi-video
--disable-oobe-chromevox-hint-timer-for-testing
--disable-oobe-network-screen-skipping-for-testing
--disable-oopr-debug-crash-dump
--disable-origin-trial-controlled-blink-features
--disable-overscroll-edge-effect
--disable-partial-raster
--disable-pdf-tagging
--disable-pepper-3d
--disable-per-user-timezone
--disable-permissions-api
--disable-pinch
--disable-pnacl-crash-throttling
--disable-policy-key-verification
--disable-popup-blocking
--disable-prefer-compositing-to-lcd-text
--disable-presentation-api
--disable-print-preview
--disable-prompt-on-repost
--disable-pull-to-refresh-effect
--disable-pushstate-throttle
--disable-reading-from-canvas
--disable-remote-fonts
--disable-remote-playback-api
--disable-renderer-accessibility
--disable-renderer-backgrounding
--disable-resource-scheduler
--disable-rgba-4444-textures
--disable-rollback-option
--disable-rtc-smoothness-algorithm
--disable-screen-orientation-lock
--disable-scroll-to-text-fragment
--disable-search-engine-choice-screen
--disable-seccomp-filter-sandbox
--disable-setuid-sandbox
--disable-shader-name-hashing
--disable-shared-workers
--disable-signin-frame-client-certs
--disable-site-isolation-for-policy
--disable-site-isolation-trials
--disable-skia-graphite
--disable-skia-runtime-opts
--disable-smooth-scrolling
--disable-software-compositing-fallback
--disable-software-rasterizer
--disable-speech-api
--disable-speech-synthesis-api
--disable-stack-profiler
--disable-system-font-check
--disable-third-party-keyboard-workaround
--disable-threaded-animation
--disable-threaded-compositing
--disable-timeouts-for-profiling
--disable-touch-drag-drop
--disable-usb-keyboard-detect
--disable-v8-idle-tasks
--disable-variations-safe-mode
--disable-variations-seed-fetch-throttling
--disable-video-capture-use-gpu-memory-buffer
--disable-virtual-keyboard
--disable-volume-adjust-sound
--disable-vsync-for-tests
--disable-vulkan-fallback-to-gl-for-testing
--disable-vulkan-for-tests
--disable-vulkan-surface
--disable-wayland-ime
--disable-web-security
--disable-webgl
--disable-webgl-image-chromium
--disable-webgl2
--disable-webrtc-encryption
--disable-yuv-image-decoding
--disable-zero-browsers-open-for-tests
--disable-zero-copy
--disable-zero-copy-dxgi-video
--disallow-lacros
--disallow-non-exact-resource-reuse
--disallow-policy-block-dev-mode
--discoverability
--document-user-activation-required
--dom-automation
--double-buffer-compositing
--draw-quad-split-limit
--draw-view-bounds-rects
--drm-virtual-connector-is-external
--dump-blink-runtime-call-stats
--dump-browser-histograms
--dump-dom
--dumpstate-path
--edge-touch-filtering
--egl
--elevate
--embedded-extension-options
--enable
--enable-accelerated-2d-canvas
--enable-adaptive-selection-handle-orientation
--enable-aggressive-domstorage-flushing
--enable-angle-features
--enable-arc
--enable-arcvm
--enable-arcvm-rt-vcpu
--enable-ash-debug-browser
--enable-audio-debug-recordings-from-extension
--enable-auto-reload
--enable-automation
--enable-background-thread-pool
--enable-background-tracing
--enable-begin-frame-control
--enable-benchmarking
--enable-ble-advertising-in-apps
--enable-blink-features
--enable-blink-test-features
--enable-bookmark-undo
--enable-caret-browsing
--enable-cast-receiver
--enable-cast-streaming-receiver
--enable-chrome-browser-cloud-management
--enable-cloud-print-proxy
--enable-consumer-kiosk
--enable-content-directories
--enable-crash-reporter
--enable-crash-reporter-for-testing
--enable-crx-hash-check
--enable-dawn-backend-validation
--enable-dawn-features
--enable-dim-shelf
--enable-dinosaur-easter-egg-alt-images
--enable-direct-composition-video-overlays
--enable-discover-feed
--enable-distillability-service
--enable-dom-distiller
--enable-domain-reliability
--enable-download-warning-improvements
--enable-encryption-selection
--enable-exclusive-audio
--enable-experimental-accessibility-autoclick
--enable-experimental-accessibility-labels-debugging
--enable-experimental-accessibility-language-detection
--enable-experimental-accessibility-language-detection-dynamic
--enable-experimental-accessibility-manifest-v3
--enable-experimental-accessibility-switch-access-text
--enable-experimental-cookie-features
--enable-experimental-extension-apis
--enable-experimental-web-platform-features
--enable-experimental-webassembly-features
--enable-extension-activity-log-testing
--enable-extension-activity-logging
--enable-extension-assets-sharing
--enable-fake-no-alloc-direct-call-for-testing
--enable-features
--enable-field-trial-config
--enable-finch-seed-delta-compression
--enable-font-antialiasing
--enable-gamepad-button-axis-events
--enable-gpu
--enable-gpu-benchmarking
--enable-gpu-blocked-time
--enable-gpu-client-logging
--enable-gpu-client-tracing
--enable-gpu-command-logging
--enable-gpu-debugging
--enable-gpu-driver-debug-logging
--enable-gpu-memory-buffer-compositor-resources
--enable-gpu-memory-buffer-video-frames
--enable-gpu-rasterization
--enable-gpu-service-logging
--enable-gpu-service-tracing
--enable-hangout-services-extension-for-testing
--enable-hardware-overlays
--enable-houdini
--enable-houdini-dlc
--enable-houdini64
--enable-idle-tracing
--enable-input
--enable-ios-handoff-to-other-devices
--enable-isolated-web-apps-in-renderer
--enable-lacros-fork-zygotes-at-login-screen
--enable-lcd-text
--enable-leak-detection
--enable-leak-detection-heap-snapshot
--enable-legacy-background-tracing
--enable-live-caption-pref-for-testing
--enable-local-file-accesses
--enable-logging
--enable-longpress-drag-selection
--enable-low-end-device-mode
--enable-low-res-tiling
--enable-magnifier-debug-draw-rect
--enable-main-frame-before-activation
--enable-nacl
--enable-nacl-debug
--enable-native-gpu-memory-buffers
--enable-natural-scroll-default
--enable-ndk-translation
--enable-ndk-translation64
--enable-net-benchmarking
--enable-network-information-downlink-max
--enable-new-app-menu-icon
--enable-ntp-search-engine-country-detection
--enable-oobe-chromevox-hint-timer-for-dev-mode
--enable-oobe-test-api
--enable-optimization-guide-debug-logs
--enable-page-content-annotations-logging
--enable-pepper-testing
--enable-pixel-output-in-tests
--enable-plugin-placeholder-testing
--enable-potentially-annoying-security-features
--enable-precise-memory-info
--enable-prefer-compositing-to-lcd-text
--enable-primary-node-access-for-vkms-testing
--enable-privacy-sandbox-ads-apis
--enable-profile-shortcut-manager
--enable-promo-manager-fullscreen-promos
--enable-protected-video-buffers
--enable-raster-side-dark-mode-for-images
--enable-requisition-edits
--enable-resources-file-sharing
--enable-rgba-4444-textures
--enable-sandbox-logging
--enable-scaling-clipped-images
--enable-service-binary-launcher
--enable-service-manager-tracing
--enable-sgi-video-sync
--enable-skia-benchmarking
--enable-skia-graphite
--enable-smooth-scrolling
--enable-spatial-navigation
--enable-speech-dispatcher
--enable-spotlight-actions
--enable-stats-collection-bindings
--enable-strict-mixed-content-checking
--enable-strict-powerful-feature-restrictions
--enable-swap-buffers-with-bounds
--enable-tablet-form-factor
--enable-third-party-keyboard-workaround
--enable-threaded-texture-mailboxes
--enable-top-drag-gesture
--enable-touch-calibration-setting
--enable-touch-drag-drop
--enable-touchpad-three-finger-click
--enable-touchview
--enable-trace-app-source
--enable-tracing
--enable-tracing-format
--enable-tracing-fraction
--enable-tracing-output
--enable-ui-devtools
--enable-unsafe-webgpu
--enable-upgrade-signin-promo
--enable-user-metrics
--enable-usermedia-screen-capturing
--enable-viewport
--enable-virtual-keyboard
--enable-vtune-support
--enable-vulkan-protected-memory
--enable-wayland-ime
--enable-wayland-server
--enable-web-auth-deprecated-mojo-testing-api
--enable-webgl-developer-extensions
--enable-webgl-draft-extensions
--enable-webgl-image-chromium
--enable-webgpu-developer-features
--enable-webrtc-srtp-encrypted-headers
--enable-widevine
--enable-zero-copy
--enabled
--encode-binary
--encrypted-reporting-url
--enforce
--enforce-gl-minimums
--enforce-webrtc-ip-permission-check
--enforce_strict
--ensure-forced-color-profile
--enterprise-disable-arc
--enterprise-enable-forced-re-enrollment
--enterprise-enable-forced-re-enrollment-on-flex
--enterprise-enable-initial-enrollment
--enterprise-enable-unified-state-determination
--enterprise-enable-zero-touch-enrollment
--enterprise-enrollment-initial-modulus
--enterprise-enrollment-modulus-limit
--enterprise-force-manual-enrollment-in-test-builds
--eol-ignore-profile-creation-time
--eol-reset-dismissed-prefs
--evaluate-type
--evaluate_capability
--explicitly-allowed-ports
--export-uma-logs-to-file
--expose-internals-for-testing
--extension-apps-block-for-app-service-in-ash
--extension-apps-run-in-ash-and-lacros
--extension-apps-run-in-ash-only
--extension-content-verification
--extension-force-channel
--extension-install-event-chrome-log-for-tests
--extension-process
--extension-updater-test-request
--extensions-install-verification
--extensions-not-webstore
--extensions-on-chrome-urls
--extensions-run-in-ash-and-lacros
--extensions-run-in-ash-only
--external-metrics-collection-interval
--extra-search-query-params
--extra-web-apps-dir
--fail-audio-stream-creation
--fake-arc-recommended-apps-for-testing
--fake-drivefs-launcher-chroot-path
--fake-drivefs-launcher-socket-path
--fake-oobe-configuration-file
--fake-variations-channel
--false
--feedback-server
--field-trial-handle
--file-storage-server-upload-url
--file-url-path-alias
--file_chooser
--finch-seed-expiration-age
--finch-seed-ignore-pending-download
--finch-seed-min-download-period
--finch-seed-min-update-period
--finch-seed-no-charging-requirement
--fingerprint-sensor-location
--first-exec-after-boot
--flag-switches-begin
--flag-switches-end
--font-cache-shared-handle
--font-render-hinting
--force-app-mode
--force-assistant-onboarding
--force-birch-fetch
--force-birch-release-notes
--force-browser-crash-on-gpu-crash
--force-browser-data-migration-for-testing
--force-caption-style
--force-color-profile
--force-cryptohome-recovery-for-testing
--force-dark-mode
--force-dev-mode-highlighting
--force-device-ownership
--force-device-scale-factor
--force-device-switcher-experience
--force-devtools-available
--force-disable-variation-ids
--force-effective-connection-type
--force-enable-metrics-reporting
--force-enable-night-mode
--force-enable-stylus-tools
--force-fieldtrial-params
--force-fieldtrials
--force-first-run
--force-first-run-ui
--force-gpu-mem-available-mb
--force-gpu-mem-discardable-limit-mb
--force-happiness-tracking-system
--force-headless-for-tests
--force-high-contrast
--force-hwid-check-result-for-test
--force-lacros-launch-at-login-screen-for-testing
--force-launch-browser
--force-login-manager-in-tests
--force-max-texture-size
--force-media-resolution-height
--force-media-resolution-width
--force-msbb-setting-on-for-ukm
--force-online-connection-state-for-indicator
--force-permission-policy-unload-default-enabled
--force-pnacl-subzero
--force-prefers-no-reduced-motion
--force-prefers-reduced-motion
--force-presentation-receiver-for-testing
--force-protected-video-output-buffers
--force-raster-color-profile
--force-refresh-rate-throttle
--force-renderer-accessibility
--force-search-engine-choice-screen
--force-separate-egl-display-for-webgl-testing
--force-show-cursor
--force-show-release-track
--force-show-update-menu-badge
--force-status-area-collapsible
--force-tablet-mode
--force-tablet-power-button
--force-text-direction
--force-ui-direction
--force-update-menu-type
--force-update-remote-url
--force-variation-ids
--force-video-overlays
--force-wave-audio
--force-webgpu-compat
--force-webrtc-ip-handling-policy
--force-webxr-runtime
--force-whats-new
--forest-feature-key
--form-factor
--full-memory-crash-report
--gaia-config
--gaia-config-contents
--gaia-url
--gamepad-polling-interval
--gcm-checkin-url
--gcm-mcs-endpoint
--gcm-registration-url
--generate-accessibility-test-expectations
--generate-pdf-document-outline
--get-access-token-for-test
--gl
--gl-egl
--gl-null
--gl-shader-interm-output
--glanceables-key
--gles
--gles-egl
--gles-null
--google-api-key
--google-apis-url
--google-base-url
--google-doodle-url
--gpu
--gpu-blocklist-test-group
--gpu-device-id
--gpu-disk-cache-size-kb
--gpu-driver-bug-list-test-group
--gpu-driver-version
--gpu-launcher
--gpu-no-context-lost
--gpu-preferences
--gpu-process
--gpu-program-cache-size-kb
--gpu-rasterization-msaa-sample-count
--gpu-revision
--gpu-sandbox-allow-sysv-shm
--gpu-sandbox-failures-fatal
--gpu-sandbox-start-early
--gpu-startup-dialog
--gpu-sub-system-id
--gpu-vendor-id
--gpu-watchdog-timeout-seconds
--gpu2-startup-dialog
--graphics-buffer-count
--growth-campaigns-path
--guest
--guest-wallpaper-large
--guest-wallpaper-small
--hardware-video-decode-framerate
--hardware_video_decoding
--hardware_video_encoding
--has-chromeos-keyboard
--has-hps
--has-internal-stylus
--has-number-pad
--headless
--help
--hermes-fake
--hidden-network-migration-age
--hidden-network-migration-interval
--hide-crash-restore-bubble
--hide-icons
--hide-scrollbars
--highlight-all-webviews
--highlight-non-lcd-text-layers
--homedir
--homepage
--host
--host-package-label
--host-package-name
--host-resolver-rules
--host-version-code
--icon_reader
--ignore-arcvm-dev-conf
--ignore-autocomplete-off-autofill
--ignore-certificate-errors-spki-list
--ignore-google-port-numbers
--ignore-gpu-blocklist
--ignore-unknown-auth-factors
--ignore-user-profile-mapping-for-tests
--ime
--in-process-broker
--in-process-gpu
--incognito
--init-isolate-as-foreground
--initial-preferences-file
--initialize-client-hints-storage
--input
--inspector-protocol-log
--install-autogenerated-theme
--install-chrome-app
--install-isolated-web-app-from-file
--install-isolated-web-app-from-url
--install-log-fast-upload-for-tests
--instant-process
--ip-address-space-overrides
--ipc-connection-timeout
--ipc-dump-directory
--ipc-fuzzer-testcase
--isolate-origins
--isolated-context-origins
--isolation-by-default
--javascript-harmony
--js-flags
--keep-alive-for-test
--kiosk
--kiosk-printing
--kiosk-splash-screen-min-time-seconds
--lacros-availability-ignore
--lacros-chrome-additional-args
--lacros-chrome-additional-args-file
--lacros-chrome-additional-env
--lacros-chrome-path
--lacros-mojo-socket-for-testing
--lacros-selection-policy-ignore
--lang
--last-launched-app
--launch-rma
--launch-time-ticks
--layer
--libassistant
--list-apps
--list-audio-devices
--llvm-profile-file
--load-and-launch-app
--load-apps
--load-extension
--load-guest-mode-test-extension
--load-signin-profile-test-extension
--loading-predictor-allow-local-request-for-testing
--localhost
--log-best-effort-tasks
--log-file
--log-gpu-control-list-decisions
--log-level
--log-missing-unload-ack
--log-net-log
--log-on-ui-double-background-blur
--login-manager
--login-profile
--login-user
--lso-url
--ltr
--mahi-feature-key
--make-chrome-default
--make-default-browser
--managed-mode
--managed-user-id
--mangle-localized-strings
--manual
--market-url-for-testing
--marketing-opt-in-url
--max-active-webgl-contexts
--max-decoded-image-size-mb
--max-gum-fps
--max-output-volume-dba1m
--max-untiled-layer-height
--max-untiled-layer-width
--max-web-media-player-count
--mem-pressure-system-reserved-kb
--memlog
--memlog-sampling-rate
--memlog-stack-mode
--message-loop-type-ui
--metal
--metal-null
--metrics-client-id
--metrics-recording-only
--metrics-shmem-handle
--metrics-upload-interval
--mf_cdm
--min-height-for-gpu-raster-tile
--min-video-decoder-output-buffer-size
--minimal
--mirroring
--mixed
--mixer-enable-dynamic-channel-count
--mixer-service-endpoint
--mixer-service-port
--mixer-source-audio-ready-threshold-ms
--mixer-source-input-queue-ms
--mock-cert-verifier-default-result-for-testing
--model-quality-service-api-key
--model-quality-service-url
--modifier-split-feature-key
--mojo-core-library-path
--mojo-is-broker
--mojo-local-storage
--monitoring-destination-id
--mse-audio-buffer-size-limit-mb
--mse-video-buffer-size-limit-mb
--mute-audio
--nacl-debug-mask
--nacl-gdb
--nacl-gdb-script
--native-messaging-connect-extension
--native-messaging-connect-host
--native-messaging-connect-id
--nearby-share-certificate-validity-period-hours
--nearby-share-device-id
--nearby-share-num-private-certificates
--nearby-share-verbose-logging
--nearbysharing-http-host
--net-log-capture-mode
--net-log-max-size-mb
--netifs-to-ignore
--network-quiet-timeout
--new-window
--no-default-browser-check
--no-delay-for-dx12-vulkan-info-collection
--no-experiments
--no-first-run
--no-mojo
--no-network-profile-warning
--no-pdf-header-footer
--no-pings
--no-pre-read-main-dll
--no-proxy-server
--no-sandbox
--no-service-autorun
--no-startup-window
--no-system-proxy-config-service
--no-unsandboxed-zygote
--no-user-gesture-required
--no-xr-runtime
--no-xshm
--no-zygote
--no-zygote-sandbox
--noerrdialogs
--note-taking-app-ids
--notification-inline-reply
--notification-launch-id
--num-raster-threads
--nv12
--oauth-account-manager-url
--oauth2-client-id
--oauth2-client-secret
--offer-in-settings
--offscreen-document-testing
--on-the-fly-mhtml-hash-computation
--ondevice-validation-request-override
--ondevice-validation-write-to-file
--ondevice_handwriting
--on_device_model_execution
--oobe-eula-url-for-tests
--oobe-force-tablet-first-run
--oobe-large-screen-special-scaling
--oobe-print-frontend-load-timings
--oobe-screenshot-dir
--oobe-show-accessibility-button-on-marketing-opt-in-for-testing
--oobe-skip-postlogin
--oobe-skip-to-login
--oobe-timer-interval
--oobe-timezone-override-for-tests
--oobe-trigger-sync-timeout-for-tests
--opengraph
--openxr
--optimization-guide-fetch-hints-override
--optimization-guide-fetch-hints-override-timer
--optimization-guide-model-execution-validate
--optimization-guide-model-override
--optimization-guide-model-validate
--optimization-guide-ondevice-model-execution-override
--optimization-guide-service-api-key
--optimization-guide-service-get-hints-url
--optimization-guide-service-get-models-url
--optimization-guide-service-model-execution-url
--optimization_guide_hints_override
--orientation-sensors
--origin-trial-disabled-features
--origin-trial-disabled-tokens
--origin-trial-public-key
--override-enabled-cdm-interface-version
--override-hardware-secure-codecs-for-testing
--override-language-detection
--override-metrics-upload-url
--override-use-software-gl-for-tests
--overview-button-for-tests
--ozone-dump-file
--ozone-override-screen-size
--ozone-platform
--ozone-platform-hint
--pack-extension
--pack-extension-key
--page-content-annotations-validation-batch-size
--page-content-annotations-validation-content-visibility
--page-content-annotations-validation-startup-delay-seconds
--page-content-annotations-validation-write-to-file
--parent-window
--passthrough
--password-store
--pdf-renderer
--pdf_conversion
--pen-devices
--perf-test-print-uma-means
--perfetto-disable-interning
--performance
--picker-feature-key
--playready-key-system
--policy

--policy-verification-key
--ppapi
--ppapi-antialiased-text-enabled
--ppapi-in-process
--ppapi-plugin-launcher
--ppapi-startup-dialog
--ppapi-subpixel-rendering-setting
--pre-crashpad-crash-test
--prediction-service-mock-likelihood
--preinstalled-web-apps-dir
--prevent-kiosk-autolaunch-for-testing
--prevent-resizing-contents-for-testing
--previous-app
--print-to-pdf
--printing-ppd-channel
--privacy-policy-host-for-tests
--private-aggregation-developer-mode
--privet-ipv6-only
--process-per-site
--process-per-tab
--product-version
--production
--profile-base-name
--profile-directory
--profile-email
--profile-management-attributes
--profile-requires-policy
--profiling-at-start
--profiling-file
--profiling-flush
--protected-audiences-consented-debug-token
--proxy-auto-detect
--proxy-bypass-list
--proxy-pac-url
--proxy-server
--proxy_resolver_win
--public-accounts-saml-acl-url
--pull-to-refresh
--purge-model-and-features-store
--purge-optimization-guide-store
--pwa-launcher-version
--qs-add-fake-bluetooth-devices
--qs-add-fake-cast-devices
--qs-show-locale-tile
--query-tiles-country-code
--query-tiles-enable-trending
--query-tiles-instant-background-task
--query-tiles-rank-tiles
--query-tiles-single-tier
--quota-change-event-interval
--raise-timer-frequency
--rdp_desktop_session
--reader-mode-feedback
--reader-mode-heuristics
--realtime-reporting-url
--redirect-libassistant-logging
--reduce-accept-language
--reduce-user-agent-minor-version
--reduce-user-agent-platform-oscpu
--register-max-dark-suspend-delay
--register-pepper-plugins
--regulatory-label-dir
--relauncher
--remote-allow-origins
--remote-debug-mode
--remote-debugging-address
--remote-debugging-io-pipes
--remote-debugging-pipe
--remote-debugging-port
--remote-debugging-socket-name
--remote-debugging-targets
--remote-reboot-command-timeout-in-seconds-for-testing
--renderer
--renderer-client-id
--renderer-cmd-prefix
--renderer-process-limit
--renderer-sampling
--renderer-startup-dialog
--renderer-wait-for-java-debugger
--renderpass
--report-vp9-as-an-unsupported-mime-type
--request-desktop-sites
--require-wlan
--reset-browsing-instance-between-tests
--reset-variation-state
--restart
--restore-key-on-lock-screen
--restore-last-session
--restrict-gamepad-access
--reven-branding
--rlz-ping-delay
--rma-not-allowed
--rtl
--run-all-compositor-stages-before-draw
--run-manual
--run-web-tests
--safe-mode
--safebrowsing-enable-enhanced-protection
--safebrowsing-manual-download-blacklist
--saml-password-change-url
--sandbox-ipc
--save-page-as-mhtml
--scheduled-reboot-grace-period-in-seconds-for-testing
--scheduler-boost-urgent
--scheduler-configuration
--scheduler-configuration-default
--screen-capture-audio-default-unchecked
--screen-config
--screenshot
--screen_ai
--seal-key
--search-engine-choice-country
--search-provider-logo-url
--secondary-display-layout
--secure-connect-api-url
--service
--service-name
--service-request-attachment-name
--service-sandbox-type
--service_with_jit
--set-extension-throttle-test-params
--setup
--shader-cache-path
--shared-array-buffer-allowed-origins
--shared-array-buffer-unrestricted-access-allowed
--shared-files
--shelf-hotseat
--shill-stub
--short-merge-session-timeout-for-test
--short-reporting-delay
--show-aggregated-damage
--show-autofill-signatures
--show-autofill-type-predictions
--show-component-extension-options
--show-composited-layer-borders
--show-dc-layer-debug-borders
--show-fps-counter
--show-icons
--show-layer-animation-bounds
--show-layout-shift-regions
--show-login-dev-overlay
--show-mac-overlay-borders
--show-oobe-dev-overlay
--show-oobe-quick-start-debugger
--show-overdraw-feedback
--show-paint-rects
--show-property-changed-rects
--show-screenspace-rects
--show-surface-damage-rects
--show-taps
--signed-out-ntp-modules
--silent-debugger-extension-api
--silent-launch
--simulate-browsing-data-lifetime
--simulate-critical-update
--simulate-elevated-recovery
--simulate-idle-timeout
--simulate-outdated
--simulate-outdated-no-au
--simulate-update-error-code
--simulate-update-hresult
--simulate-upgrade
--single-process
--site-per-process
--skia-font-cache-limit-mb
--skia-graphite-backend
--skia-resource-cache-limit-mb
--skip-force-online-signin-for-testing
--skip-local-upm-gms-core-version-check-for-testing
--skip-multidevice-screen
--skip-reorder-nudge-show-threshold-duration
--slow-down-compositing-scale-factor
--slow-down-raster-scale-factor
--sms-test-messages
--source-shortcut
--speech_recognition
--ssl-key-log-file
--ssl-version-max
--ssl-version-min
--stabilize-time-dependent-view-for-tests
--stable-release-mode
--staging
--start-fullscreen
--start-maximized
--start-stack-profiler
--start-stack-profiler-with-java-name-hashing
--suppress-message-center-popups
--system-aec-enabled
--system-developer-mode
--system-font-family
--system-log-upload-frequency
--test-encryption-migration-ui
--test-memory-log-delay-in-minutes
--test-name
--test-register-standard-scheme
--test-third-party-cookie-phaseout
--test-type
--test-wallpaper-server
--tether-host-scans-ignore-wired-connections
--tether-stub
--time-before-onboarding-survey-in-seconds-for-testing
--time-ticks-at-unix-epoch
--time-zone-for-testing
--timeout
--tls1.2
--tls1.3
--top-chrome-touch-ui
--top-controls-hide-threshold
--top-controls-show-threshold
--touch-events
--tpm-is-dynamic
--trace-config-file
--trace-smb-size
--trace-startup
--trace-startup-duration
--trace-startup-enable-privacy-filtering
--trace-startup-file
--trace-startup-format
--trace-startup-owner
--trace-startup-record-mode
--trace-to-console
--trace-to-file
--trace-to-file-name
--translate-ranker-model-url
--translate-script-url
--translate-security-origin
--trusted-download-sources
--try-supported-channel-layouts
--type
--ui-disable-partial-swap
--ui-enable-layer-lists
--ui-toolkit
--ukm-server-url
--uma-insecure-server-url
--uma-server-url
--unfiltered-bluetooth-devices
--uninstall
--uninstall-app-id
--unlimited-storage
--unsafely-allow-protected-media-identifier-for-domain
--unsafely-treat-insecure-origin-as-secure
--use-adapter-luid
--use-angle
--use-cast-browser-pref-config
--use-cmd-decoder
--use-cras
--use-fake-codec-for-peer-connection
--use-fake-cras-audio-client-for-dbus
--use-fake-device-for-media-stream
--use-fake-mahi-manager
--use-fake-mjpeg-decode-accelerator
--use-fake-ui-for-digital-identity
--use-fake-ui-for-fedcm
--use-fake-ui-for-media-stream
--use-file-for-fake-audio-capture
--use-file-for-fake-video-capture
--use-first-display-as-internal
--use-first-party-set
--use-gl
--use-gpu-high-thread-priority-for-perf-tests
--use-gpu-in-tests
--use-heap-profiling-proto-writer
--use-legacy-metrics-service
--use-mobile-user-agent
--use-mock-cert-verifier-for-testing
--use-mock-keychain
--use-myfiles-in-user-data-dir-for-testing
--use-redist-dml
--use-related-website-set
--use-system-clipboard
--use-system-default-printer
--use-system-proxy-resolver
--use-va-dev-keys
--use-vulkan
--use-wayland-explicit-grab
--user-agent
--user-agent-product
--user-data-dir
--user-data-migrated
--user-gesture-required
--utility
--utility-and-browser
--utility-cmd-prefix
--utility-sampling
--utility-startup-dialog
--utility-sub-type
--v
--v8-cache-options
--validate-crx
--validate-input-event-stream
--validating
--variations-insecure-server-url
--variations-override-country
--variations-seed-fetch-interval
--variations-seed-version
--variations-server-url
--variations-test-seed-path
--verbose-logging-in-nacl
--version
--video-capture-use-gpu-memory-buffer
--video-image-texture-target
--video-threads
--view-stack-traces
--virtual-time-budget
--viz-demo-use-gpu
--vmodule
--vsync-interval
--vulkan
--vulkan-heap-memory-limit-mb
--vulkan-null
--vulkan-sync-cpu-memory-limit-mb
--wait-for-debugger
--wait-for-debugger-children
--wait-for-debugger-on-navigation
--wait-for-debugger-webui
--wallet-service-use-sandbox
--waveout-buffers
--web-otp-backend
--web-otp-backend-auto
--web-otp-backend-sms-verification
--web-otp-backend-user-consent
--web-sql-access
--web-ui-data-source-path-for-testing
--webapk-server-url
--webauthn-permit-enterprise-attestation
--webauthn-remote-desktop-support
--webauthn-remote-proxied-requests-allowed-additional-origin
--webgl-antialiasing-mode
--webgl-msaa-sample-count
--webrtc-event-log-proactive-pruning-delta
--webrtc-event-log-upload-delay-ms
--webrtc-event-log-upload-no-suppression
--webrtc-event-logging
--webrtc-ip-handling-policy
--webview-disable-app-recovery
--webview-disable-safebrowsing-support
--webview-draw-functor-uses-vulkan
--webview-enable-app-recovery
--webview-enable-modern-cookie-same-site
--webview-enable-trust-tokens-component
--webview-fenced-frames
--webview-force-crash-java
--webview-force-crash-native
--webview-force-disable-3pcs
--webview-fps-component
--webview-log-js-console-messages
--webview-safebrowsing-block-all-resources
--webview-sandboxed-renderer
--webview-selective-image-inversion-darkening
--webview-tpcd-metadata-component
--webview-verbose-logging
--win-jumplist-action
--window-name
--window-position
--window-size
--window-workspace
--winhttp-proxy-resolver
--wm-window-animations-disabled
--xr_compositing
--xsession_chooser
--yuy2
--zygote
```
