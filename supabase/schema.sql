-- =============================================================================
-- UM STUDIO — Esquema PostgreSQL / Supabase para "La Clase Viva" & Adjuntos
-- =============================================================================

-- 1. Tabla: temas_estudio (Contenido oficial sincronizado con el aula)
create table if not exists public.temas_estudio (
  id text primary key,
  nombre_asignatura text not null,
  numero_tema integer not null check (numero_tema > 0),
  objetivo text not null,
  concepto_clave_latex text not null,
  ejemplo text not null,
  sincronizacion_porcentaje integer not null default 94,
  updated_at timestamptz not null default now()
);

-- 2. Tabla: notas_adjuntos_estudiante (Apuntes personales, PDFs y fotos de tablero)
create table if not exists public.notas_adjuntos_estudiante (
  id uuid primary key default gen_random_uuid(),
  tema_id text not null references public.temas_estudio(id) on delete cascade,
  usuario_id text not null,
  tipo_archivo text not null check (tipo_archivo in ('pdf', 'imagen', 'nota')),
  url_archivo text,
  nombre_archivo text,
  peso_bytes bigint,
  contenido_nota text,
  updated_at timestamptz not null default now(),
  created_at timestamptz not null default now()
);

create index if not exists idx_notas_adjuntos_tema_usuario
  on public.notas_adjuntos_estudiante (tema_id, usuario_id);

-- 3. Habilitar Supabase Realtime para lectura reactiva en vivo
alter publication supabase_realtime add table public.temas_estudio;
alter publication supabase_realtime add table public.notas_adjuntos_estudiante;

-- 4. Semilla inicial de asignaturas (Ing. Energética • Unimagdalena)
insert into public.temas_estudio (
  id,
  nombre_asignatura,
  numero_tema,
  objetivo,
  concepto_clave_latex,
  ejemplo,
  sincronizacion_porcentaje
) values
  (
    'fisica',
    'Física Mecánica y Termodinámica',
    2,
    'Comprender la segunda ley de Newton en sistemas inerciales y cuantificar el efecto disipativo de la fuerza de rozamiento cinético y estático sobre cuerpos rígidos.',
    '\sum \vec{F} = m \cdot \vec{a} \quad ; \quad f_k = \mu_k \cdot N',
    'Un bloque de masa m sobre una superficie horizontal rugosa experimenta una fuerza normal N = m·g y una oposición cinética f_k = μ_k·N. Si se aplica una tracción horizontal F, la aceleración resultante del sistema es a = (F − μ_k·m·g) / m.',
    94
  ),
  (
    'calculo',
    'Cálculo Diferencial e Integral',
    4,
    'Dominar la técnica de integración por partes derivada de la regla del producto para resolver integrales de funciones trascendentes acopladas con polinomios.',
    '\int u \, dv = u \cdot v - \int v \, du',
    'Para evaluar la integral de x·e^x dx, seleccionamos u = x (cuya derivada simplifica el grado algebraico, du = dx) y dv = e^x dx (con antiderivada inmediata v = e^x), obteniendo x·e^x − e^x + C.',
    96
  ),
  (
    'electricidad',
    'Fundamentos de Electricidad',
    3,
    'Reducir cualquier red eléctrica lineal bilateral de dos terminales a un circuito equivalente de Thévenin o Norton para analizar transferencia máxima de potencia en cargas variables.',
    'V_{\text{th}} = I_{\text{N}} \cdot R_{\text{th}} \quad ; \quad P_{\max} = \frac{V_{\text{th}}^2}{4 R_{\text{th}}}',
    'Al desconectar la resistencia de carga R_L y pasivar las fuentes independientes (fuentes de tensión en cortocircuito y de corriente en circuito abierto), se determina R_th vista desde los terminales A-B y la tensión en vacío V_th.',
    92
  ),
  (
    'algebra',
    'Álgebra Lineal',
    5,
    'Representar transformaciones lineales entre espacios vectoriales de dimensión finita mediante matrices asociadas y caracterizar su núcleo (ker) e imagen (im).',
    'T(\alpha \vec{u} + \beta \vec{v}) = \alpha T(\vec{u}) + \beta T(\vec{v}) \quad ; \quad \dim(V) = \text{nul}(T) + \text{rg}(T)',
    'Una rotación antihoraria de 90° en ℝ² preserva combinaciones lineales y se representa respecto a la base canónica mediante la matriz ortogonal A = [[0, −1], [1, 0]], con núcleo trivial ker(T) = {0}.',
    91
  )
on conflict (id) do update set
  nombre_asignatura = excluded.nombre_asignatura,
  numero_tema = excluded.numero_tema,
  objetivo = excluded.objetivo,
  concepto_clave_latex = excluded.concepto_clave_latex,
  ejemplo = excluded.ejemplo,
  sincronizacion_porcentaje = excluded.sincronizacion_porcentaje,
  updated_at = now();

-- 5. Bucket institucional de almacenamiento ("adjuntos_estudio")
insert into storage.buckets (id, name, public)
values ('adjuntos_estudio', 'adjuntos_estudio', true)
on conflict (id) do nothing;
