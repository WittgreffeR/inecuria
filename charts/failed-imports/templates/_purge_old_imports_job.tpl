{{/* vim: set filetype=mustache: */}}

{{- define "purgeOldImports.job" -}}
metadata:
  name: {{ template "failed-imports.fullname" . }}-purge-old-imports
  labels:
    {{- include "failed-imports.commonLabels" . | nindent 4 }}
    app.kubernetes.io/component: purge-old-imports
spec:
  restartPolicy: Never
  containers:
    - name: purge-old-imports
      image: "{{ .Values.app.django.image.repository }}:{{ default .Values.app.django.image.tag .Chart.AppVersion }}"
      command: ["/bin/sh"]
      args: ["-ec", "python manage.py purge_old_imports {{ .Values.app.purgeOldImports.days }}"]
      envFrom:
        - secretRef:
            name: {{ template "failed-imports.fullname" . }}-purge-old-imports-secrets
      env:
      {{- range $key, $value := .Values.app.env }}
        - name: "{{ $key }}"
          value: "{{ $value }}"
      {{- end }}
      {{- range $key, $value := .Values.app.django.env }}
        - name: "{{ $key }}"
          value: "{{ $value }}"
      {{- end }}
        - name: "CHART"
          value: {{ .Chart.Name }}-{{ .Chart.Version }}
{{- end -}}

