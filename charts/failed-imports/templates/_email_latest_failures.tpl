{{/* vim: set filetype=mustache: */}}

{{- define "emailLatestFailures.job" -}}
metadata:
  name: {{ template "failed-imports.fullname" . }}-email-latest-failures
  labels:
    {{- include "failed-imports.commonLabels" . | nindent 4 }}
    app.kubernetes.io/component: email-latest-failures
spec:
  restartPolicy: Never
  containers:
    - name: email-latest-failures
      image: "{{ .Values.app.django.image.repository }}:{{ default .Values.app.django.image.tag .Chart.AppVersion }}"
      command: ["/bin/sh"]
      args: ["-ec", "python manage.py email_latest_failures {{ .Values.app.emailLatestFailures.values.days }} '{{ .Values.app.emailLatestFailures.values.emails }}'"]
      envFrom:
        - secretRef:
            name: {{ template "failed-imports.fullname" . }}-email-latest-failures-secrets
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
