# Documento de Requisitos del Producto (Product Requirements Document): NX8020 - Página de Validación MVP
**Versión:** 2.1  
**Fecha:** 28 de Junio, 2024  
**Autor:** Equipo de Producto  
**Estado:** Aprobado para Desarrollo  

## 1. Visión General y Visión (Overview & Vision)

**NX8020** es una herramienta B2B SaaS propuesta que combina Minería de Procesos (Process Mining) con una IA conversacional activada por voz para ayudar a las empresas a descubrir y corregir ineficiencias operacionales.

Este documento describe los requisitos para un sitio web de marketing de una sola página. El propósito principal de esta página no es ser un producto completo, sino un Producto Mínimo Viable (MVP) para validar el interés del mercado. Educará a clientes potenciales sobre la propuesta de valor central, les permitirá experimentar una demostración simulada de nuestra IA activada por voz principal, y capturará leads a través de una lista de espera (waitlist) para un futuro programa beta y campaña de email.

## 2. Objetivos Empresariales y Métricas de Éxito (Business Goals & Success Metrics)

El éxito de este proyecto se medirá por su capacidad de lograr los siguientes objetivos dentro de los primeros 60 días del lanzamiento:

### Objetivo Principal: Validar la Necesidad del Mercado para el Producto Central
- **Métrica 1 (Conversión):** Lograr 150+ registros en la lista de espera (waitlist sign-ups)
- **Métrica 2 (Engagement):** Registrar 200+ interacciones únicas con el Demo de IA, confirmando que los usuarios están interactuando con la característica principal

### Objetivo Secundario: Construir una Lista de Prospectos para Marketing Futuro
- **Métrica:** Crear una base de datos limpia y calificada de al menos 150 prospectos (nombre, email de trabajo, preferencia de idioma) en MySQL

### Objetivo Terciario: Recopilar Retroalimentación Cualitativa (Qualitative Feedback)
- **Métrica 1 (Contacto Directo):** Iniciar al menos 15 conversaciones directas con prospectos interesados vía el canal integrado de WhatsApp
- **Métrica 2 (Análisis de Interés):** Analizar logs de interacción del demo para identificar cuál pregunta preprogramada ("factura", "incorporación", "pedidos") se activa más frecuentemente, indicando el punto de dolor más resonante

## 3. Audiencia Objetivo y Persona (Target Audience & Persona)

**Industrias:** Logística y Cadena de Suministro (Supply Chain), Servicios Financieros (ej. procesamiento de préstamos), Manufactura, Telecomunicaciones, Administración de Salud.

### Persona Principal: "Alex Chen, Director de Operaciones"
- **Rol:** Director de Operaciones en una empresa logística de tamaño medio
- **Responsabilidades:** Supervisar todo el proceso de pedido a cobro (order-to-cash), reducir tiempos de entrega, y gestionar costos operacionales
- **Puntos de Dolor:**
  - "Sé que hay cuellos de botella (bottlenecks), pero no puedo identificarlos sin auditorías manuales tediosas"
  - "Nuestros datos están dispersos en nuestro ERP, CRM, y software de envíos. Es difícil obtener una vista única"
  - "Las herramientas BI son poderosas pero requieren un analista de datos para construir reportes. Necesito respuestas más rápidas"
- **Objetivos:** Encontrar una herramienta que proporcione insights claros y accionables sin una curva de aprendizaje empinada o involucramiento pesado de TI

## 4. Diseño e Identidad Visual (Design & Visual Identity)

El diseño debe sentirse profesional, confiable e innovador. El tema visual es "Claridad desde la Complejidad" (Clarity from Complexity).

### Paleta de Colores (Color Palette):
- **Primario:** Azul Profundo (#0A2540) - Profesionalismo, datos, estabilidad
- **Secundario:** Blanco Limpio/Gris Claro (#FFFFFF, #F6F9FC) - Fondo, espacio abierto
- **Acento:** Verde Azulado Vibrante (#00C49A) - Innovación, eficiencia, CTAs
- **Texto:** Gris Oscuro (#333333) - Legibilidad

### Tipografía (Typography):
- **Encabezados:** Inter o Montserrat
- **Texto del Cuerpo:** Lato o Open Sans

### Imágenes y Visuales (Imagery & Visuals):
- **Imagen Hero:** Visualización abstracta de flujos de datos moviéndose del caos al orden
- **Visual de Minería de Procesos:** Infografía simplificada "antes-y-después" mostrando un proceso optimizado
- **Visual Co-piloto IA:** Gráfico que combina un ícono de voz (micrófono) con un ícono de datos (gráfico)

## 5. Flujo de Usuario y Requisitos Funcionales (User Flow & Functional Requirements)

### Flujo de Usuario:
Llega a la Página → Lee Hero y Propuestas de Valor → Se desplaza a la sección "Co-piloto IA" → Hace clic en "Probar Demo en Vivo" → Interactúa con IA simulada en un modal → Cierra modal → Hace clic en "Unirse a Lista de Espera" o se desplaza al formulario → Llena Nombre/Email → Hace clic en "Obtener Acceso Temprano" → Ve Mensaje de Éxito/Error

### Historias de Usuario (Requisitos Funcionales):

#### Página y Funcionalidad Central
- **FR-1: Visualización de Página:** Como visitante, quiero ver una página de aterrizaje única y responsiva que funcione en escritorio, tablet y móvil
- **FR-2: Selección de Idioma:** Como visitante, quiero alternar todo el contenido de la página entre Inglés (US) y Español (MX) con un solo clic
- **FR-3: Registro en Lista de Espera:** Como prospecto interesado, quiero enviar mi nombre y email de trabajo en un formulario para ser agregado a la lista de espera
- **FR-4: Retroalimentación del Formulario (Éxito):** Como usuario que envía el formulario correctamente, quiero ver un mensaje de éxito claro ("¡Gracias!") y que el formulario se reinicie
- **FR-5: Retroalimentación del Formulario (Error):** Como usuario, si ingreso un email inválido o si mi email ya está en la lista, quiero ver un mensaje de error claro y útil
- **FR-6: Contacto Directo:** Como prospecto con preguntas, quiero hacer clic en un enlace para iniciar una conversación prellenada en WhatsApp
- **FR-7: Captura de Datos:** Como propietario del producto, cada envío exitoso del formulario debe guardarse como una nueva entrada en una base de datos MySQL, capturando el nombre del usuario, email, timestamp de envío, e idioma elegido

#### Demo de IA Simulada
- **FR-8: Iniciar Demo:** Como visitante, quiero hacer clic en un botón "Probar Demo en Vivo" para abrir una simulación de IA interactiva en una ventana modal
- **FR-9: Entrada de Voz y Permiso:** Como usuario, quiero hacer clic en un ícono de micrófono y otorgar permiso al navegador (browser) para escuchar mi pregunta hablada
- **FR-10: Preguntas Guiadas:** Como usuario, quiero ver una lista de preguntas sugeridas dentro del modal del demo para saber qué preguntar para una interacción exitosa
- **FR-11: Respuesta Enlatada:** Como usuario, cuando mi pregunta hablada contiene una palabra clave reconocida (ej. "factura"), quiero escuchar y ver una respuesta relevante preprogramada de la "IA"
- **FR-12: Respuesta de Respaldo (Fallback):** Como usuario, si hago una pregunta no reconocida, quiero recibir una respuesta de respaldo elegante (ej. "Actualmente estoy entrenado en ejemplos específicos. Intenta preguntar sobre 'tiempo de aprobación de facturas'") para guiarme de vuelta al camino previsto
- **FR-13: Retroalimentación Visual:** Como usuario, quiero ver señales visuales (ej. ícono de micrófono pulsante, cambios de texto de estado) que me muestren si la aplicación está inactiva, escuchando, procesando, o respondiendo
- **FR-14: Registro de Interacción del Demo:** Como propietario del producto, cada vez que un usuario active una respuesta enlatada (no de respaldo), quiero registrar esta interacción (ej. vía console.log simple o un evento de analytics futuro) para rastrear qué características son más interesantes

## 6. Requisitos No Funcionales (Non-Functional Requirements)

- **NFR-1: Rendimiento (Performance):** La página debe cargar en menos de 3 segundos y lograr un puntaje de Google PageSpeed Insights de 85+ para móvil y escritorio
- **NFR-2: Seguridad (Security):** Todas las entradas de usuario deben ser sanitizadas en el backend (Flask/Python) para prevenir inyección SQL
- **NFR-3: Compatibilidad de Navegador (Browser Compatibility):** El sitio debe renderizarse correctamente en las últimas dos versiones de Chrome, Firefox, Safari, y Edge. El demo de IA debe funcionar en navegadores que soporten la Web Speech API (principalmente Chrome y Edge). Un mensaje indicando incompatibilidad debe mostrarse en otros (ej. Firefox)
- **NFR-4: Accesibilidad (Accessibility):** La página debe seguir las pautas básicas WCAG 2.1 AA (contraste de color, etiquetas de formulario, texto alt, atributos ARIA para el modal)

## 7. Stack Tecnológico (Technical Stack)

- **Frontend:** HTML5, CSS3, JavaScript (ES6+)
- **API Clave:** Web Speech API (SpeechRecognition y SpeechSynthesis)
- **Backend:** Python 3.9+ con el framework Flask
- **Base de Datos (Database):** MySQL 5.7+
- **Infraestructura:** GoDaddy Hosting (cPanel) usando la característica "Setup Python App". Los manejadores Apache enrutarán las solicitudes /api a la aplicación Flask

## 8. Alcance Futuro (Fuera del Alcance para este MVP)

Las siguientes características están explícitamente fuera del alcance para esta página de validación inicial:

- Un backend de IA real y funcional (ej. usando modelos NLP). El demo es una simulación frontend
- Funcionalidad de cuentas de usuario y login
- Procesamiento real de datos o integración con sistemas de clientes (CRMs, ERPs)
- Sitio web de múltiples páginas (ej. blog, acerca de nosotros, página de precios)
- Respondedores automáticos de email
- Integración avanzada de analytics (más allá del registro básico)

## 9. Términos Técnicos en Español (Spanish Technical Terms)

Para facilitar la comprensión en mercados de habla hispana, se incluyen las siguientes traducciones de términos técnicos clave:

- **Process Mining:** Minería de Procesos
- **Bottleneck:** Cuello de Botella
- **Workflow:** Flujo de Trabajo
- **Dashboard:** Panel de Control
- **Analytics:** Análisis/Analítica
- **Insights:** Perspectivas/Conocimientos
- **API:** Interfaz de Programación de Aplicaciones
- **Database:** Base de Datos
- **Backend:** Sistema de Fondo
- **Frontend:** Interfaz de Usuario
- **Browser:** Navegador
- **Onboarding:** Incorporación
- **Order Fulfillment:** Cumplimiento de Pedidos
- **Picking Stage:** Etapa de Recolección
- **Pre-boarding Checklist:** Lista de Verificación Previa
- **Voice Recognition:** Reconocimiento de Voz
- **Natural Language Processing:** Procesamiento de Lenguaje Natural
- **Real-time:** Tiempo Real
- **Waitlist:** Lista de Espera
- **Lead Generation:** Generación de Prospectos
- **Conversion Rate:** Tasa de Conversión
- **User Experience (UX):** Experiencia de Usuario
- **User Interface (UI):** Interfaz de Usuario
- **Responsive Design:** Diseño Responsivo
- **Performance Optimization:** Optimización de Rendimiento