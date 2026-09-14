; ModuleID = 'algorithms/02_c/sorting/insertion_sort.c'
source_filename = "algorithms/02_c/sorting/insertion_sort.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str = private unnamed_addr constant [50 x i8] c"[C InsertionSort] FAILED: not sorted at index %d\0A\00", align 1
@.str.1 = private unnamed_addr constant [45 x i8] c"[C InsertionSort] Insertion sort verified: {\00", align 1
@.str.2 = private unnamed_addr constant [5 x i8] c"%d%s\00", align 1
@.str.3 = private unnamed_addr constant [3 x i8] c", \00", align 1
@.str.4 = private unnamed_addr constant [3 x i8] c"}\0A\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable
define dso_local void @insertion_sort(ptr noundef captures(none) %0, i32 noundef %1) local_unnamed_addr #0 {
  %3 = icmp sgt i32 %1, 1
  br i1 %3, label %4, label %6

4:                                                ; preds = %2
  %5 = zext nneg i32 %1 to i64
  br label %7

6:                                                ; preds = %20, %2
  ret void

7:                                                ; preds = %4, %20
  %8 = phi i64 [ 1, %4 ], [ %25, %20 ]
  %9 = getelementptr inbounds nuw i32, ptr %0, i64 %8
  %10 = load i32, ptr %9, align 4, !tbaa !5
  br label %11

11:                                               ; preds = %7, %17
  %12 = phi i64 [ %8, %7 ], [ %13, %17 ]
  %13 = add nsw i64 %12, -1
  %14 = getelementptr inbounds nuw i32, ptr %0, i64 %13
  %15 = load i32, ptr %14, align 4, !tbaa !5
  %16 = icmp sgt i32 %15, %10
  br i1 %16, label %17, label %20

17:                                               ; preds = %11
  %18 = getelementptr inbounds nuw i32, ptr %0, i64 %12
  store i32 %15, ptr %18, align 4, !tbaa !5
  %19 = icmp sgt i64 %12, 1
  br i1 %19, label %11, label %20, !llvm.loop !9

20:                                               ; preds = %17, %11
  %21 = phi i64 [ 0, %17 ], [ %12, %11 ]
  %22 = shl i64 %21, 32
  %23 = ashr exact i64 %22, 30
  %24 = getelementptr inbounds i8, ptr %0, i64 %23
  store i32 %10, ptr %24, align 4, !tbaa !5
  %25 = add nuw nsw i64 %8, 1
  %26 = icmp eq i64 %25, %5
  br i1 %26, label %6, label %7, !llvm.loop !11
}

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.start.p0(ptr captures(none)) #1

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.end.p0(ptr captures(none)) #1

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #2 {
  %1 = alloca <4 x i32>, align 16
  %2 = alloca i32, align 16
  %3 = alloca i32, align 4
  %4 = alloca i32, align 8
  %5 = alloca i32, align 4
  %6 = alloca i32, align 16
  %7 = alloca i32, align 4
  call void @llvm.lifetime.start.p0(ptr nonnull %1)
  call void @llvm.lifetime.start.p0(ptr nonnull %2)
  call void @llvm.lifetime.start.p0(ptr nonnull %3)
  call void @llvm.lifetime.start.p0(ptr nonnull %4)
  call void @llvm.lifetime.start.p0(ptr nonnull %5)
  call void @llvm.lifetime.start.p0(ptr nonnull %6)
  call void @llvm.lifetime.start.p0(ptr nonnull %7)
  store <4 x i32> <i32 33, i32 7, i32 91, i32 12>, ptr %1, align 16
  store i32 5, ptr %2, align 16
  store i32 5, ptr %3, align 4
  store i32 78, ptr %4, align 8
  store i32 2, ptr %5, align 4
  store i32 44, ptr %6, align 16
  store i32 19, ptr %7, align 4
  store <4 x i32> <i32 7, i32 12, i32 33, i32 91>, ptr %1, align 16, !tbaa !5
  %8 = load i32, ptr %2, align 16, !tbaa !5
  %9 = icmp slt i32 %8, 91
  %10 = getelementptr inbounds nuw i8, ptr %1, i64 4
  %11 = getelementptr inbounds nuw i8, ptr %1, i64 8
  %12 = getelementptr inbounds nuw i8, ptr %1, i64 4
  %13 = getelementptr inbounds nuw i8, ptr %1, i64 12
  %14 = getelementptr inbounds nuw i8, ptr %1, i64 8
  %15 = getelementptr inbounds nuw i8, ptr %1, i64 4
  %16 = getelementptr inbounds nuw i8, ptr %1, i64 8
  %17 = getelementptr inbounds nuw i8, ptr %1, i64 12
  %18 = getelementptr inbounds nuw i8, ptr %1, i64 4
  %19 = getelementptr inbounds nuw i8, ptr %1, i64 12
  %20 = getelementptr inbounds nuw i8, ptr %1, i64 8
  %21 = getelementptr inbounds nuw i8, ptr %1, i64 4
  %22 = getelementptr inbounds nuw i8, ptr %1, i64 12
  %23 = getelementptr inbounds nuw i8, ptr %1, i64 8
  %24 = getelementptr inbounds nuw i8, ptr %1, i64 4
  %25 = getelementptr inbounds nuw i8, ptr %1, i64 8
  %26 = getelementptr inbounds nuw i8, ptr %1, i64 12
  br i1 %9, label %27, label %43

27:                                               ; preds = %0
  %28 = getelementptr inbounds nuw i8, ptr %1, i64 12
  store i32 91, ptr %2, align 16, !tbaa !5
  %29 = getelementptr inbounds nuw i8, ptr %1, i64 8
  %30 = load i32, ptr %29, align 8, !tbaa !5
  %31 = icmp sgt i32 %30, %8
  br i1 %31, label %32, label %43

32:                                               ; preds = %27
  %33 = getelementptr inbounds nuw i8, ptr %1, i64 12
  store i32 %30, ptr %33, align 4, !tbaa !5
  %34 = getelementptr inbounds nuw i8, ptr %1, i64 4
  %35 = load i32, ptr %34, align 4, !tbaa !5
  %36 = icmp sgt i32 %35, %8
  br i1 %36, label %37, label %43

37:                                               ; preds = %32
  %38 = getelementptr inbounds nuw i8, ptr %1, i64 8
  store i32 %35, ptr %38, align 8, !tbaa !5
  %39 = load i32, ptr %1, align 16, !tbaa !5
  %40 = icmp sgt i32 %39, %8
  br i1 %40, label %41, label %43

41:                                               ; preds = %37
  %42 = getelementptr inbounds nuw i8, ptr %1, i64 4
  store i32 %39, ptr %42, align 4, !tbaa !5
  br label %43

43:                                               ; preds = %41, %37, %32, %27, %0
  %44 = phi ptr [ %1, %41 ], [ %2, %0 ], [ %28, %27 ], [ %10, %37 ], [ %11, %32 ]
  store i32 %8, ptr %44, align 4, !tbaa !5
  %45 = load i32, ptr %3, align 4, !tbaa !5
  %46 = load i32, ptr %2, align 16, !tbaa !5
  %47 = icmp sgt i32 %46, %45
  br i1 %47, label %48, label %67

48:                                               ; preds = %43
  store i32 %46, ptr %3, align 4, !tbaa !5
  %49 = getelementptr inbounds nuw i8, ptr %1, i64 12
  %50 = load i32, ptr %49, align 4, !tbaa !5
  %51 = icmp sgt i32 %50, %45
  br i1 %51, label %52, label %67

52:                                               ; preds = %48
  store i32 %50, ptr %2, align 16, !tbaa !5
  %53 = getelementptr inbounds nuw i8, ptr %1, i64 8
  %54 = load i32, ptr %53, align 8, !tbaa !5
  %55 = icmp sgt i32 %54, %45
  br i1 %55, label %56, label %67

56:                                               ; preds = %52
  %57 = getelementptr inbounds nuw i8, ptr %1, i64 12
  store i32 %54, ptr %57, align 4, !tbaa !5
  %58 = getelementptr inbounds nuw i8, ptr %1, i64 4
  %59 = load i32, ptr %58, align 4, !tbaa !5
  %60 = icmp sgt i32 %59, %45
  br i1 %60, label %61, label %67

61:                                               ; preds = %56
  %62 = getelementptr inbounds nuw i8, ptr %1, i64 8
  store i32 %59, ptr %62, align 8, !tbaa !5
  %63 = load i32, ptr %1, align 16, !tbaa !5
  %64 = icmp sgt i32 %63, %45
  br i1 %64, label %65, label %67

65:                                               ; preds = %61
  %66 = getelementptr inbounds nuw i8, ptr %1, i64 4
  store i32 %63, ptr %66, align 4, !tbaa !5
  br label %67

67:                                               ; preds = %65, %61, %56, %52, %48, %43
  %68 = phi ptr [ %1, %65 ], [ %3, %43 ], [ %2, %48 ], [ %12, %61 ], [ %13, %52 ], [ %14, %56 ]
  store i32 %45, ptr %68, align 4, !tbaa !5
  %69 = load i32, ptr %4, align 8, !tbaa !5
  %70 = load i32, ptr %3, align 4, !tbaa !5
  %71 = icmp sgt i32 %70, %69
  br i1 %71, label %72, label %94

72:                                               ; preds = %67
  store i32 %70, ptr %4, align 8, !tbaa !5
  %73 = load i32, ptr %2, align 16, !tbaa !5
  %74 = icmp sgt i32 %73, %69
  br i1 %74, label %75, label %94

75:                                               ; preds = %72
  store i32 %73, ptr %3, align 4, !tbaa !5
  %76 = getelementptr inbounds nuw i8, ptr %1, i64 12
  %77 = load i32, ptr %76, align 4, !tbaa !5
  %78 = icmp sgt i32 %77, %69
  br i1 %78, label %79, label %94

79:                                               ; preds = %75
  store i32 %77, ptr %2, align 16, !tbaa !5
  %80 = getelementptr inbounds nuw i8, ptr %1, i64 8
  %81 = load i32, ptr %80, align 8, !tbaa !5
  %82 = icmp sgt i32 %81, %69
  br i1 %82, label %83, label %94

83:                                               ; preds = %79
  %84 = getelementptr inbounds nuw i8, ptr %1, i64 12
  store i32 %81, ptr %84, align 4, !tbaa !5
  %85 = getelementptr inbounds nuw i8, ptr %1, i64 4
  %86 = load i32, ptr %85, align 4, !tbaa !5
  %87 = icmp sgt i32 %86, %69
  br i1 %87, label %88, label %94

88:                                               ; preds = %83
  %89 = getelementptr inbounds nuw i8, ptr %1, i64 8
  store i32 %86, ptr %89, align 8, !tbaa !5
  %90 = load i32, ptr %1, align 16, !tbaa !5
  %91 = icmp sgt i32 %90, %69
  br i1 %91, label %92, label %94

92:                                               ; preds = %88
  %93 = getelementptr inbounds nuw i8, ptr %1, i64 4
  store i32 %90, ptr %93, align 4, !tbaa !5
  br label %94

94:                                               ; preds = %92, %88, %83, %79, %75, %72, %67
  %95 = phi ptr [ %1, %92 ], [ %4, %67 ], [ %3, %72 ], [ %15, %88 ], [ %2, %75 ], [ %16, %83 ], [ %17, %79 ]
  store i32 %69, ptr %95, align 4, !tbaa !5
  %96 = load i32, ptr %5, align 4, !tbaa !5
  %97 = load i32, ptr %4, align 8, !tbaa !5
  %98 = icmp sgt i32 %97, %96
  br i1 %98, label %99, label %124

99:                                               ; preds = %94
  store i32 %97, ptr %5, align 4, !tbaa !5
  %100 = load i32, ptr %3, align 4, !tbaa !5
  %101 = icmp sgt i32 %100, %96
  br i1 %101, label %102, label %124

102:                                              ; preds = %99
  store i32 %100, ptr %4, align 8, !tbaa !5
  %103 = load i32, ptr %2, align 16, !tbaa !5
  %104 = icmp sgt i32 %103, %96
  br i1 %104, label %105, label %124

105:                                              ; preds = %102
  store i32 %103, ptr %3, align 4, !tbaa !5
  %106 = getelementptr inbounds nuw i8, ptr %1, i64 12
  %107 = load i32, ptr %106, align 4, !tbaa !5
  %108 = icmp sgt i32 %107, %96
  br i1 %108, label %109, label %124

109:                                              ; preds = %105
  store i32 %107, ptr %2, align 16, !tbaa !5
  %110 = getelementptr inbounds nuw i8, ptr %1, i64 8
  %111 = load i32, ptr %110, align 8, !tbaa !5
  %112 = icmp sgt i32 %111, %96
  br i1 %112, label %113, label %124

113:                                              ; preds = %109
  %114 = getelementptr inbounds nuw i8, ptr %1, i64 12
  store i32 %111, ptr %114, align 4, !tbaa !5
  %115 = getelementptr inbounds nuw i8, ptr %1, i64 4
  %116 = load i32, ptr %115, align 4, !tbaa !5
  %117 = icmp sgt i32 %116, %96
  br i1 %117, label %118, label %124

118:                                              ; preds = %113
  %119 = getelementptr inbounds nuw i8, ptr %1, i64 8
  store i32 %116, ptr %119, align 8, !tbaa !5
  %120 = load i32, ptr %1, align 16, !tbaa !5
  %121 = icmp sgt i32 %120, %96
  br i1 %121, label %122, label %124

122:                                              ; preds = %118
  %123 = getelementptr inbounds nuw i8, ptr %1, i64 4
  store i32 %120, ptr %123, align 4, !tbaa !5
  br label %124

124:                                              ; preds = %122, %118, %113, %109, %105, %102, %99, %94
  %125 = phi ptr [ %1, %122 ], [ %5, %94 ], [ %4, %99 ], [ %18, %118 ], [ %3, %102 ], [ %19, %109 ], [ %2, %105 ], [ %20, %113 ]
  store i32 %96, ptr %125, align 4, !tbaa !5
  %126 = load i32, ptr %6, align 16, !tbaa !5
  %127 = load i32, ptr %5, align 4, !tbaa !5
  %128 = icmp sgt i32 %127, %126
  br i1 %128, label %129, label %157

129:                                              ; preds = %124
  store i32 %127, ptr %6, align 16, !tbaa !5
  %130 = load i32, ptr %4, align 8, !tbaa !5
  %131 = icmp sgt i32 %130, %126
  br i1 %131, label %132, label %157

132:                                              ; preds = %129
  store i32 %130, ptr %5, align 4, !tbaa !5
  %133 = load i32, ptr %3, align 4, !tbaa !5
  %134 = icmp sgt i32 %133, %126
  br i1 %134, label %135, label %157

135:                                              ; preds = %132
  store i32 %133, ptr %4, align 8, !tbaa !5
  %136 = load i32, ptr %2, align 16, !tbaa !5
  %137 = icmp sgt i32 %136, %126
  br i1 %137, label %138, label %157

138:                                              ; preds = %135
  store i32 %136, ptr %3, align 4, !tbaa !5
  %139 = getelementptr inbounds nuw i8, ptr %1, i64 12
  %140 = load i32, ptr %139, align 4, !tbaa !5
  %141 = icmp sgt i32 %140, %126
  br i1 %141, label %142, label %157

142:                                              ; preds = %138
  store i32 %140, ptr %2, align 16, !tbaa !5
  %143 = getelementptr inbounds nuw i8, ptr %1, i64 8
  %144 = load i32, ptr %143, align 8, !tbaa !5
  %145 = icmp sgt i32 %144, %126
  br i1 %145, label %146, label %157

146:                                              ; preds = %142
  %147 = getelementptr inbounds nuw i8, ptr %1, i64 12
  store i32 %144, ptr %147, align 4, !tbaa !5
  %148 = getelementptr inbounds nuw i8, ptr %1, i64 4
  %149 = load i32, ptr %148, align 4, !tbaa !5
  %150 = icmp sgt i32 %149, %126
  br i1 %150, label %151, label %157

151:                                              ; preds = %146
  %152 = getelementptr inbounds nuw i8, ptr %1, i64 8
  store i32 %149, ptr %152, align 8, !tbaa !5
  %153 = load i32, ptr %1, align 16, !tbaa !5
  %154 = icmp sgt i32 %153, %126
  br i1 %154, label %155, label %157

155:                                              ; preds = %151
  %156 = getelementptr inbounds nuw i8, ptr %1, i64 4
  store i32 %153, ptr %156, align 4, !tbaa !5
  br label %157

157:                                              ; preds = %155, %151, %146, %142, %138, %135, %132, %129, %124
  %158 = phi ptr [ %1, %155 ], [ %6, %124 ], [ %5, %129 ], [ %21, %151 ], [ %4, %132 ], [ %22, %142 ], [ %3, %135 ], [ %23, %146 ], [ %2, %138 ]
  store i32 %126, ptr %158, align 4, !tbaa !5
  %159 = load i32, ptr %7, align 4, !tbaa !5
  %160 = load i32, ptr %6, align 16, !tbaa !5
  %161 = icmp sgt i32 %160, %159
  br i1 %161, label %162, label %193

162:                                              ; preds = %157
  store i32 %160, ptr %7, align 4, !tbaa !5
  %163 = load i32, ptr %5, align 4, !tbaa !5
  %164 = icmp sgt i32 %163, %159
  br i1 %164, label %165, label %193

165:                                              ; preds = %162
  store i32 %163, ptr %6, align 16, !tbaa !5
  %166 = load i32, ptr %4, align 8, !tbaa !5
  %167 = icmp sgt i32 %166, %159
  br i1 %167, label %168, label %193

168:                                              ; preds = %165
  store i32 %166, ptr %5, align 4, !tbaa !5
  %169 = load i32, ptr %3, align 4, !tbaa !5
  %170 = icmp sgt i32 %169, %159
  br i1 %170, label %171, label %193

171:                                              ; preds = %168
  store i32 %169, ptr %4, align 8, !tbaa !5
  %172 = load i32, ptr %2, align 16, !tbaa !5
  %173 = icmp sgt i32 %172, %159
  br i1 %173, label %174, label %193

174:                                              ; preds = %171
  store i32 %172, ptr %3, align 4, !tbaa !5
  %175 = getelementptr inbounds nuw i8, ptr %1, i64 12
  %176 = load i32, ptr %175, align 4, !tbaa !5
  %177 = icmp sgt i32 %176, %159
  br i1 %177, label %178, label %193

178:                                              ; preds = %174
  store i32 %176, ptr %2, align 16, !tbaa !5
  %179 = getelementptr inbounds nuw i8, ptr %1, i64 8
  %180 = load i32, ptr %179, align 8, !tbaa !5
  %181 = icmp sgt i32 %180, %159
  br i1 %181, label %182, label %193

182:                                              ; preds = %178
  %183 = getelementptr inbounds nuw i8, ptr %1, i64 12
  store i32 %180, ptr %183, align 4, !tbaa !5
  %184 = getelementptr inbounds nuw i8, ptr %1, i64 4
  %185 = load i32, ptr %184, align 4, !tbaa !5
  %186 = icmp sgt i32 %185, %159
  br i1 %186, label %187, label %193

187:                                              ; preds = %182
  %188 = getelementptr inbounds nuw i8, ptr %1, i64 8
  store i32 %185, ptr %188, align 8, !tbaa !5
  %189 = load i32, ptr %1, align 16, !tbaa !5
  %190 = icmp sgt i32 %189, %159
  br i1 %190, label %191, label %193

191:                                              ; preds = %187
  %192 = getelementptr inbounds nuw i8, ptr %1, i64 4
  store i32 %189, ptr %192, align 4, !tbaa !5
  br label %193

193:                                              ; preds = %191, %187, %182, %178, %174, %171, %168, %165, %162, %157
  %194 = phi ptr [ %1, %191 ], [ %7, %157 ], [ %6, %162 ], [ %24, %187 ], [ %5, %165 ], [ %2, %174 ], [ %4, %168 ], [ %25, %182 ], [ %3, %171 ], [ %26, %178 ]
  store i32 %159, ptr %194, align 4, !tbaa !5
  %195 = load i32, ptr %1, align 16, !tbaa !5
  %196 = getelementptr inbounds nuw i8, ptr %1, i64 4
  %197 = load i32, ptr %196, align 4, !tbaa !5
  %198 = icmp sgt i32 %195, %197
  br i1 %198, label %237, label %199

199:                                              ; preds = %193
  %200 = getelementptr inbounds nuw i8, ptr %1, i64 8
  %201 = load i32, ptr %200, align 8, !tbaa !5
  %202 = icmp sgt i32 %197, %201
  br i1 %202, label %237, label %203

203:                                              ; preds = %199
  %204 = getelementptr inbounds nuw i8, ptr %1, i64 12
  %205 = load i32, ptr %204, align 4, !tbaa !5
  %206 = icmp sgt i32 %201, %205
  br i1 %206, label %237, label %207

207:                                              ; preds = %203
  %208 = load i32, ptr %2, align 16, !tbaa !5
  %209 = icmp sgt i32 %205, %208
  br i1 %209, label %237, label %210

210:                                              ; preds = %207
  %211 = load i32, ptr %3, align 4, !tbaa !5
  %212 = icmp sgt i32 %208, %211
  br i1 %212, label %237, label %213

213:                                              ; preds = %210
  %214 = load i32, ptr %4, align 8, !tbaa !5
  %215 = icmp sgt i32 %211, %214
  br i1 %215, label %237, label %216

216:                                              ; preds = %213
  %217 = load i32, ptr %5, align 4, !tbaa !5
  %218 = icmp sgt i32 %214, %217
  br i1 %218, label %237, label %219

219:                                              ; preds = %216
  %220 = load i32, ptr %6, align 16, !tbaa !5
  %221 = icmp sgt i32 %217, %220
  br i1 %221, label %237, label %222

222:                                              ; preds = %219
  %223 = load i32, ptr %7, align 4, !tbaa !5
  %224 = icmp sgt i32 %220, %223
  br i1 %224, label %237, label %225

225:                                              ; preds = %222
  %226 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.1)
  %227 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %195, ptr noundef nonnull @.str.3)
  %228 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %197, ptr noundef nonnull @.str.3)
  %229 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %201, ptr noundef nonnull @.str.3)
  %230 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %205, ptr noundef nonnull @.str.3)
  %231 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %208, ptr noundef nonnull @.str.3)
  %232 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %211, ptr noundef nonnull @.str.3)
  %233 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %214, ptr noundef nonnull @.str.3)
  %234 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %217, ptr noundef nonnull @.str.3)
  %235 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %220, ptr noundef nonnull @.str.3)
  %236 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %223, ptr noundef nonnull @.str.4)
  br label %240

237:                                              ; preds = %222, %219, %216, %213, %210, %207, %203, %199, %193
  %238 = phi i32 [ 1, %193 ], [ 2, %199 ], [ 3, %203 ], [ 4, %207 ], [ 5, %210 ], [ 6, %213 ], [ 7, %216 ], [ 8, %219 ], [ 9, %222 ]
  %239 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str, i32 noundef %238)
  br label %240

240:                                              ; preds = %225, %237
  %241 = phi i32 [ 1, %237 ], [ 0, %225 ]
  call void @llvm.lifetime.end.p0(ptr nonnull %1)
  call void @llvm.lifetime.end.p0(ptr nonnull %2)
  call void @llvm.lifetime.end.p0(ptr nonnull %3)
  call void @llvm.lifetime.end.p0(ptr nonnull %4)
  call void @llvm.lifetime.end.p0(ptr nonnull %5)
  call void @llvm.lifetime.end.p0(ptr nonnull %6)
  call void @llvm.lifetime.end.p0(ptr nonnull %7)
  ret i32 %241
}

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr noundef readonly captures(none), ...) local_unnamed_addr #3

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite) }
attributes #2 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { nofree nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = distinct !{!9, !10}
!10 = !{!"llvm.loop.mustprogress"}
!11 = distinct !{!11, !10}
