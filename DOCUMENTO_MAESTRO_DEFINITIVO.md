# DOCUMENTO MAESTRO DEFINITIVO

## SISTEMA WEB PRIVADO PARA LECTURA DE DESPRENDIBLES DE PAGO

### CÁLCULO AUTOMÁTICO DE CAPACIDAD DE ENDEUDAMIENTO (CDE)

---

## 1. PROPÓSITO DEL SISTEMA

Este sistema es una **plataforma web privada y segura**, diseñada para:

1. **Leer automáticamente** desprendibles de pago y nóminas (PDF o imagen).
2. **Extraer información financiera precisa y estructurada** de cada documento.
3. **Calcular automáticamente la Capacidad de Endeudamiento (CDE)** aplicando reglas estrictas.
4. **Permitir simulación de compra de cartera**, ajustando los pasivos seleccionados.
5. **Registrar historial completo y auditar cada cálculo**, garantizando trazabilidad.
6. **Eliminar errores humanos** y digitación manual.

**Principio clave:** el usuario **no ingresa valores financieros manualmente**; solo puede corregir casos excepcionales, como pagaduría incorrecta.

---

## 2. ACCESO Y CONTROL DEL SISTEMA

### 2.1 Usuario raíz (Administrador General)

* Único usuario raíz creado manualmente.
* Credenciales:

  * Correo: `solucionesfinancierasssc@gmail.com`
  * Contraseña: `Fonsofi1218`
* Funciones:

  * Crear, modificar y eliminar usuarios.
  * Asignar roles y permisos.
  * Bloquear o autorizar accesos.
  * Configurar catálogos de pagadurías, márgenes y sectores.
  * Visualizar **historial completo** y auditoría de todos los documentos.

**Seguridad:** este usuario tiene permisos absolutos y no puede ser eliminado desde la interfaz normal.

---

### 2.2 Usuarios del sistema

| Usuario  | Contraseña | Rol                   | Funciones principales                                         |
| -------- | ---------- | --------------------- | ------------------------------------------------------------- |
| Santiago | 1218       | Administrador General | Control total, usuarios, roles, historial                     |
| Yiramar  | 0817       | Administradora        | Subir documentos, simular compra de cartera, historial propio |
| Yadira   | 1126       | Administradora        | Subir documentos, simular compra de cartera, historial propio |
| Yinayu   | 0116       | Asesor                | Subir documentos, historial propio                            |
| Mariafe  | 1224       | Asesor                | Subir documentos, historial propio                            |
| prueba   | 1221       | Asesor                | Subir documentos, historial propio                            |

**Notas de seguridad y permisos:**

* **Administrador General:** acceso total a todos los módulos y datos.
* **Administradoras:** acceso a sus propios documentos y simulaciones; pueden administrar ajustes internos según permisos.
* **Asesores:** solo pueden subir documentos y ver su propio historial.
* Ningún usuario puede ver información de otros usuarios, **excepto el Administrador General**.
* Todas las contraseñas iniciales deben cambiarse en el primer acceso.

---

## 3. ROLES Y PERMISOS

| Rol                   | Funciones                                                                | Restricciones                           |
| --------------------- | ------------------------------------------------------------------------ | --------------------------------------- |
| Público               | Calcular CDE sin guardar historial                                       | No registra documentos, no ve historial |
| Asesor                | Subir documentos, ver y editar su historial                              | No ve datos de otros usuarios           |
| Administradora        | Igual que Asesor + puede administrar ciertos ajustes internos            | No ve datos de otros usuarios           |
| Administrador General | Acceso total: usuarios, roles, historial, pagadurías, márgenes, sectores | Acceso completo a todos los datos       |

---

## 4. FLUJO COMPLETO DEL USUARIO

1. **Inicio de sesión** (correo y contraseña).
2. **Verificación opcional por SMS** (doble factor de autenticación).
3. **Carga de documento** (PDF o imagen).
4. **Vista previa automática** del documento.
5. **Extracción automática de datos**:

   * OCR avanzado
   * Normalización de nombres y valores monetarios
   * Identificación de conceptos de ingreso, salud y pasivos
6. **Presentación de datos detectados** al usuario:

   * Corrección manual de pagaduría si OCR falla
7. **Cálculo automático de CDE** usando la fórmula final:

   ```
   Ingreso neto = Ingreso total – Salud
   Capacidad neta = (Ingreso neto ÷ 2) – Margen
   CDE = Capacidad neta – Pasivos (sin contar salud)
   CDE con compra = CDE + Cartera seleccionada para compra
   ```
8. **Simulación de compra de cartera**: selección de pasivos que se suman al CDE.
9. **Guardado de historial completo** según rol del usuario.
10. **Descarga de evidencias**: documento original, informe de cálculo, detalle de pasivos, simulación de compra.

---

## 5. LECTURA AUTOMÁTICA DEL DOCUMENTO

Datos detectados automáticamente:

* Nombre completo del cliente
* Pagaduría
* Tipo de vínculo: pensionado o trabajador activo
* Fecha del documento
* Fecha y hora de lectura
* Usuario que realiza la carga

**Tecnología recomendada:** OCR avanzado + preprocesamiento de imagen + validación de patrones de texto.

---

## 6. DETECCIÓN DE INGRESOS

Conceptos válidos:

* Salario / ingreso salario
* Pensión / mesada / pensión de gracia
* Honorarios (si aplica)

**Proceso:**

1. Detección automática de todos los conceptos monetarios.
2. Suma de todos los ingresos → **Ingreso total**.
3. Validación de duplicados y consistencia.

---

## 7. DETECCIÓN DE SALUD

Conceptos detectables: Salud, EPS, ADRES, FOSYGA, 4% SERVIMEDIC, 1% CASURAUTOM

**Reglas:**

* Se descuenta **solo una vez**.
* No se incluye como pasivo ni puede restar nuevamente.
* Evita dobles descuentos que afecten la CDE.

---

## 8. DETECCIÓN DE PASIVOS Y DEDUCCIONES

Se consideran automáticamente:

* Valores negativos
* Libranzas, bancos, cooperativas
* Embargos y descuentos judiciales

**Ejemplos:** LAGOGO, Banco Popular, Excelcredit, Embargos

**Regla clave:** salud nunca se considera pasivo.

**Proceso interno:**

1. Identificación por patrones y palabras clave.
2. Clasificación por tipo (banco, cooperativa, judicial).
3. Suma de todos los pasivos para el cálculo de CDE.

---

## 9. FÓRMULA DEFINITIVA DE CÁLCULO (CDE)

```
Ingreso neto = Ingreso total – Salud
Capacidad neta = (Ingreso neto ÷ 2) – Margen
CDE = Capacidad neta – Pasivos (sin contar Salud)
CDE con compra = CDE + Cartera seleccionada para compra
```

**Notas:**

* Margen se obtiene automáticamente según la pagaduría oficial.
* Salud no se cuenta como pasivo.
* CDE con compra permite sumar pasivos seleccionados que se van a refinanciar.

---

## 10. SIMULACIÓN DE COMPRA DE CARTERA

* Tabla con todos los pasivos detectados.
* Casilla de selección por pasivo:

  * ❌ No seleccionado → se resta
  * ✅ Seleccionado → se suma al CDE con compra

**Fórmula:**

```
CDE NUEVA = CDE + Cartera seleccionada para compra
```

---

## 11. PAGADURÍAS OFICIALES

| Pagaduría                | Margen | Sector   |
| ------------------------ | ------ | -------- |
| COLPENSIONES             | 3000   | NACIONAL |
| FOPEP                    | 5000   | NACIONAL |
| FIDUPREVISORA            | 5100   | NACIONAL |
| POSITIVA                 | 5000   | NACIONAL |
| CASUR                    | 20000  | NACIONAL |
| CREMIL                   | 10000  | NACIONAL |
| COLFONDOS                | 5000   | PRIVADO  |
| MAPFRE                   | 5100   | PRIVADO  |
| PORVENIR                 | 5000   | PRIVADO  |
| SEGUROS ALFA             | 5000   | PRIVADO  |
| SKANDIA                  | 5000   | PRIVADO  |
| SURA                     | 5000   | PRIVADO  |
| ARL SURA                 | 5000   | PRIVADO  |
| PROTECCION               | 3000   | PRIVADO  |
| ASULADO                  | 3000   | PRIVADO  |
| SECRETARÍAS DE EDUCACIÓN | 20000  | SEC EDU  |

* Detectadas automáticamente, con posibilidad de corrección manual.

---

## 12. HISTORIAL Y TRAZABILIDAD

* Registro de usuario, rol, fecha/hora
* Nombre del cliente, pagaduría
* Ingreso total, salud, pasivos
* CDE original y CDE con compra
* Archivo original renombrado con nombre del cliente

---

## 13. DESCARGA DE EVIDENCIAS

* Documento original
* Informe de cálculo
* Detalle de pasivos
* Simulación de compra de cartera

**Identificación completa:** cliente, usuario, fecha, hora, pagaduría.

---

## 14. INTEGRACIÓN CON GOOGLE SHEETS

* Cada documento genera automáticamente una fila en la hoja.
* Evita errores de digitación manual.
* Permite reportes masivos y seguimiento.

---

## 15. ARQUITECTURA RECOMENDADA

**Frontend:** React o Vue.js, interfaz responsiva y segura.
**Backend:** Python + FastAPI / Node.js, microservicios para OCR y cálculo.
**Base de datos:** PostgreSQL o MySQL.
**Servicios externos:** Google Sheets API, SMS gateway.
**Seguridad:** HTTPS, hash de contraseñas (bcrypt), control de roles.
**Escalabilidad:** microservicios independientes, registro centralizado de auditoría.

---

## 16. CIERRE FINAL

El sistema:

* Aplica la lógica real de nómina y libranzas
* Evita dobles descuentos
* Permite auditoría total y trazabilidad
* Escalable y listo para producción

**Próximos pasos:**

1. Crear **diagrama de flujo completo del sistema**
2. Transformar procesos en **tareas técnicas y backlog de desarrollo**
3. Desarrollar **código base final** con OCR, cálculo, almacenamiento y reporte

---

Si quieres, puedo hacer **el diagrama visual completo**, mostrando:

* Flujo de usuarios y roles
* Extracción de datos
* Cálculo CDE
* Simulación de compra
* Integración con Google Sheets
* Auditoría y trazabilidad

Esto dejaría el documento **totalmente listo para entrega al equipo de desarrollo**.

---

Si quieres, lo hago **ahora mismo** y te lo muestro en un esquema visual claro.

¿Lo hago?
