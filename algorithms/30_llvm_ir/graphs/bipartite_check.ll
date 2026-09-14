; ModuleID = 'algorithms/02_c/graphs/bipartite_check.c'
source_filename = "algorithms/02_c/graphs/bipartite_check.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@str = private unnamed_addr constant [53 x i8] c"[C Bipartite] FAILED: even cycle should be bipartite\00", align 1
@str.3 = private unnamed_addr constant [38 x i8] c"[C Bipartite] 2-colorability verified\00", align 1
@str.4 = private unnamed_addr constant [55 x i8] c"[C Bipartite] FAILED: triangle should not be bipartite\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(argmem: read) uwtable
define dso_local range(i32 0, 2) i32 @is_bipartite(ptr noundef readonly captures(none) %0, i32 noundef %1) local_unnamed_addr #0 {
  %3 = alloca [100 x i32], align 16
  %4 = alloca [100 x i32], align 16
  call void @llvm.lifetime.start.p0(ptr nonnull %3) #5
  %5 = icmp sgt i32 %1, 0
  br i1 %5, label %6, label %57

6:                                                ; preds = %2
  %7 = zext nneg i32 %1 to i64
  %8 = shl nuw nsw i64 %7, 2
  call void @llvm.memset.p0.i64(ptr nonnull align 16 %3, i8 -1, i64 %8, i1 false), !tbaa !5
  %9 = zext nneg i32 %1 to i64
  br label %10

10:                                               ; preds = %6, %54
  %11 = phi i64 [ 0, %6 ], [ %55, %54 ]
  %12 = getelementptr inbounds nuw i32, ptr %3, i64 %11
  %13 = load i32, ptr %12, align 4, !tbaa !5
  %14 = icmp eq i32 %13, -1
  br i1 %14, label %15, label %54

15:                                               ; preds = %10
  store i32 0, ptr %12, align 4, !tbaa !5
  call void @llvm.lifetime.start.p0(ptr nonnull %4) #5
  %16 = trunc nuw nsw i64 %11 to i32
  store i32 %16, ptr %4, align 16, !tbaa !5
  br label %21

17:                                               ; preds = %49
  %18 = sext i32 %50 to i64
  %19 = icmp slt i64 %24, %18
  br i1 %19, label %21, label %20

20:                                               ; preds = %17
  call void @llvm.lifetime.end.p0(ptr nonnull %4) #5
  br label %54

21:                                               ; preds = %17, %15
  %22 = phi i64 [ 0, %15 ], [ %24, %17 ]
  %23 = phi i32 [ 1, %15 ], [ %50, %17 ]
  %24 = add nuw nsw i64 %22, 1
  %25 = getelementptr inbounds nuw i32, ptr %4, i64 %22
  %26 = load i32, ptr %25, align 4, !tbaa !5
  %27 = sext i32 %26 to i64
  %28 = getelementptr inbounds [100 x i32], ptr %0, i64 %27
  %29 = getelementptr inbounds i32, ptr %3, i64 %27
  br label %30

30:                                               ; preds = %21, %49
  %31 = phi i64 [ 0, %21 ], [ %51, %49 ]
  %32 = phi i32 [ %23, %21 ], [ %50, %49 ]
  %33 = getelementptr inbounds nuw i32, ptr %28, i64 %31
  %34 = load i32, ptr %33, align 4, !tbaa !5
  %35 = icmp eq i32 %34, 0
  br i1 %35, label %49, label %36

36:                                               ; preds = %30
  %37 = getelementptr inbounds nuw i32, ptr %3, i64 %31
  %38 = load i32, ptr %37, align 4, !tbaa !5
  %39 = icmp eq i32 %38, -1
  %40 = load i32, ptr %29, align 4, !tbaa !5
  br i1 %39, label %41, label %47

41:                                               ; preds = %36
  %42 = xor i32 %40, 1
  store i32 %42, ptr %37, align 4, !tbaa !5
  %43 = add nsw i32 %32, 1
  %44 = sext i32 %32 to i64
  %45 = getelementptr inbounds i32, ptr %4, i64 %44
  %46 = trunc nuw nsw i64 %31 to i32
  store i32 %46, ptr %45, align 4, !tbaa !5
  br label %49

47:                                               ; preds = %36
  %48 = icmp eq i32 %38, %40
  br i1 %48, label %53, label %49

49:                                               ; preds = %41, %47, %30
  %50 = phi i32 [ %43, %41 ], [ %32, %47 ], [ %32, %30 ]
  %51 = add nuw nsw i64 %31, 1
  %52 = icmp eq i64 %51, %9
  br i1 %52, label %17, label %30, !llvm.loop !9

53:                                               ; preds = %47
  call void @llvm.lifetime.end.p0(ptr nonnull %4) #5
  br label %57

54:                                               ; preds = %20, %10
  %55 = add nuw nsw i64 %11, 1
  %56 = icmp eq i64 %55, %9
  br i1 %56, label %57, label %10, !llvm.loop !11

57:                                               ; preds = %54, %2, %53
  %58 = phi i32 [ 0, %53 ], [ 1, %2 ], [ 1, %54 ]
  call void @llvm.lifetime.end.p0(ptr nonnull %3) #5
  ret i32 %58
}

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.start.p0(ptr captures(none)) #1

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.end.p0(ptr captures(none)) #1

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #2 {
  %1 = alloca [100 x i32], align 16
  %2 = alloca [100 x i32], align 16
  %3 = alloca [100 x i32], align 16
  %4 = alloca [100 x i32], align 16
  %5 = alloca [100 x [100 x i32]], align 16
  %6 = alloca [100 x [100 x i32]], align 16
  call void @llvm.lifetime.start.p0(ptr nonnull %5) #5
  call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(40000) %5, i8 0, i64 40000, i1 false)
  call void @llvm.lifetime.start.p0(ptr nonnull %6) #5
  call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(40000) %6, i8 0, i64 40000, i1 false)
  %7 = getelementptr inbounds nuw i8, ptr %5, i64 400
  store i32 1, ptr %7, align 16, !tbaa !5
  %8 = getelementptr inbounds nuw i8, ptr %5, i64 4
  store i32 1, ptr %8, align 4, !tbaa !5
  %9 = getelementptr inbounds nuw i8, ptr %5, i64 804
  store i32 1, ptr %9, align 4, !tbaa !5
  %10 = getelementptr inbounds nuw i8, ptr %5, i64 408
  store i32 1, ptr %10, align 8, !tbaa !5
  %11 = getelementptr inbounds nuw i8, ptr %5, i64 1200
  %12 = getelementptr inbounds nuw i8, ptr %5, i64 1208
  store i32 1, ptr %12, align 8, !tbaa !5
  %13 = getelementptr inbounds nuw i8, ptr %5, i64 812
  store i32 1, ptr %13, align 4, !tbaa !5
  %14 = getelementptr inbounds nuw i8, ptr %5, i64 12
  store i32 1, ptr %14, align 4, !tbaa !5
  store i32 1, ptr %11, align 16, !tbaa !5
  %15 = getelementptr inbounds nuw i8, ptr %6, i64 400
  store i32 1, ptr %15, align 16, !tbaa !5
  %16 = getelementptr inbounds nuw i8, ptr %6, i64 4
  store i32 1, ptr %16, align 4, !tbaa !5
  %17 = getelementptr inbounds nuw i8, ptr %6, i64 800
  %18 = getelementptr inbounds nuw i8, ptr %6, i64 804
  store i32 1, ptr %18, align 4, !tbaa !5
  %19 = getelementptr inbounds nuw i8, ptr %6, i64 408
  store i32 1, ptr %19, align 8, !tbaa !5
  %20 = getelementptr inbounds nuw i8, ptr %6, i64 8
  store i32 1, ptr %20, align 8, !tbaa !5
  store i32 1, ptr %17, align 16, !tbaa !5
  call void @llvm.lifetime.start.p0(ptr nonnull %3) #5
  call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(16) %3, i8 -1, i64 16, i1 false), !tbaa !5
  %21 = getelementptr inbounds nuw i8, ptr %3, i64 4
  %22 = getelementptr inbounds nuw i8, ptr %3, i64 8
  %23 = getelementptr inbounds nuw i8, ptr %3, i64 12
  br label %24

24:                                               ; preds = %114, %0
  %25 = phi i64 [ 0, %0 ], [ %115, %114 ]
  %26 = getelementptr inbounds nuw i32, ptr %3, i64 %25
  %27 = load i32, ptr %26, align 4, !tbaa !5
  %28 = icmp eq i32 %27, -1
  br i1 %28, label %29, label %114

29:                                               ; preds = %24
  store i32 0, ptr %26, align 4, !tbaa !5
  call void @llvm.lifetime.start.p0(ptr nonnull %4) #5
  %30 = trunc nuw nsw i64 %25 to i32
  store i32 %30, ptr %4, align 16, !tbaa !5
  %31 = load i32, ptr %3, align 16
  %32 = load i32, ptr %21, align 4
  %33 = load i32, ptr %22, align 8
  %34 = load i32, ptr %23, align 4
  br label %36

35:                                               ; preds = %109
  call void @llvm.lifetime.end.p0(ptr nonnull %4) #5
  br label %114

36:                                               ; preds = %109, %29
  %37 = phi i32 [ %34, %29 ], [ %110, %109 ]
  %38 = phi i32 [ %33, %29 ], [ %94, %109 ]
  %39 = phi i32 [ %32, %29 ], [ %78, %109 ]
  %40 = phi i32 [ %31, %29 ], [ %62, %109 ]
  %41 = phi i64 [ 0, %29 ], [ %43, %109 ]
  %42 = phi i32 [ 1, %29 ], [ %111, %109 ]
  %43 = add nuw nsw i64 %41, 1
  %44 = getelementptr inbounds nuw i32, ptr %4, i64 %41
  %45 = load i32, ptr %44, align 4, !tbaa !5
  %46 = sext i32 %45 to i64
  %47 = getelementptr inbounds [100 x i32], ptr %5, i64 %46
  %48 = getelementptr inbounds i32, ptr %3, i64 %46
  %49 = load i32, ptr %47, align 16, !tbaa !5
  %50 = icmp eq i32 %49, 0
  br i1 %50, label %61, label %51

51:                                               ; preds = %36
  %52 = icmp eq i32 %40, -1
  %53 = load i32, ptr %48, align 4, !tbaa !5
  br i1 %52, label %54, label %59

54:                                               ; preds = %51
  %55 = xor i32 %53, 1
  store i32 %55, ptr %3, align 16, !tbaa !5
  %56 = add nsw i32 %42, 1
  %57 = sext i32 %42 to i64
  %58 = getelementptr inbounds i32, ptr %4, i64 %57
  store i32 0, ptr %58, align 4, !tbaa !5
  br label %61

59:                                               ; preds = %51
  %60 = icmp eq i32 %40, %53
  br i1 %60, label %117, label %61

61:                                               ; preds = %59, %54, %36
  %62 = phi i32 [ %55, %54 ], [ %40, %59 ], [ %40, %36 ]
  %63 = phi i32 [ %56, %54 ], [ %42, %59 ], [ %42, %36 ]
  %64 = getelementptr inbounds nuw i8, ptr %47, i64 4
  %65 = load i32, ptr %64, align 4, !tbaa !5
  %66 = icmp eq i32 %65, 0
  br i1 %66, label %77, label %67

67:                                               ; preds = %61
  %68 = icmp eq i32 %39, -1
  %69 = load i32, ptr %48, align 4, !tbaa !5
  br i1 %68, label %72, label %70

70:                                               ; preds = %67
  %71 = icmp eq i32 %39, %69
  br i1 %71, label %117, label %77

72:                                               ; preds = %67
  %73 = xor i32 %69, 1
  store i32 %73, ptr %21, align 4, !tbaa !5
  %74 = add nsw i32 %63, 1
  %75 = sext i32 %63 to i64
  %76 = getelementptr inbounds i32, ptr %4, i64 %75
  store i32 1, ptr %76, align 4, !tbaa !5
  br label %77

77:                                               ; preds = %72, %70, %61
  %78 = phi i32 [ %73, %72 ], [ %39, %70 ], [ %39, %61 ]
  %79 = phi i32 [ %74, %72 ], [ %63, %70 ], [ %63, %61 ]
  %80 = getelementptr inbounds nuw i8, ptr %47, i64 8
  %81 = load i32, ptr %80, align 8, !tbaa !5
  %82 = icmp eq i32 %81, 0
  br i1 %82, label %93, label %83

83:                                               ; preds = %77
  %84 = icmp eq i32 %38, -1
  %85 = load i32, ptr %48, align 4, !tbaa !5
  br i1 %84, label %88, label %86

86:                                               ; preds = %83
  %87 = icmp eq i32 %38, %85
  br i1 %87, label %117, label %93

88:                                               ; preds = %83
  %89 = xor i32 %85, 1
  store i32 %89, ptr %22, align 8, !tbaa !5
  %90 = add nsw i32 %79, 1
  %91 = sext i32 %79 to i64
  %92 = getelementptr inbounds i32, ptr %4, i64 %91
  store i32 2, ptr %92, align 4, !tbaa !5
  br label %93

93:                                               ; preds = %88, %86, %77
  %94 = phi i32 [ %89, %88 ], [ %38, %86 ], [ %38, %77 ]
  %95 = phi i32 [ %90, %88 ], [ %79, %86 ], [ %79, %77 ]
  %96 = getelementptr inbounds nuw i8, ptr %47, i64 12
  %97 = load i32, ptr %96, align 4, !tbaa !5
  %98 = icmp eq i32 %97, 0
  br i1 %98, label %109, label %99

99:                                               ; preds = %93
  %100 = icmp eq i32 %37, -1
  %101 = load i32, ptr %48, align 4, !tbaa !5
  br i1 %100, label %104, label %102

102:                                              ; preds = %99
  %103 = icmp eq i32 %37, %101
  br i1 %103, label %117, label %109

104:                                              ; preds = %99
  %105 = xor i32 %101, 1
  store i32 %105, ptr %23, align 4, !tbaa !5
  %106 = add nsw i32 %95, 1
  %107 = sext i32 %95 to i64
  %108 = getelementptr inbounds i32, ptr %4, i64 %107
  store i32 3, ptr %108, align 4, !tbaa !5
  br label %109

109:                                              ; preds = %104, %102, %93
  %110 = phi i32 [ %105, %104 ], [ %37, %102 ], [ %37, %93 ]
  %111 = phi i32 [ %106, %104 ], [ %95, %102 ], [ %95, %93 ]
  %112 = sext i32 %111 to i64
  %113 = icmp slt i64 %43, %112
  br i1 %113, label %36, label %35

114:                                              ; preds = %35, %24
  %115 = add nuw nsw i64 %25, 1
  %116 = icmp eq i64 %115, 4
  br i1 %116, label %118, label %24, !llvm.loop !11

117:                                              ; preds = %102, %86, %70, %59
  call void @llvm.lifetime.end.p0(ptr nonnull %4) #5
  call void @llvm.lifetime.end.p0(ptr nonnull %3) #5
  br label %198

118:                                              ; preds = %114
  call void @llvm.lifetime.end.p0(ptr nonnull %3) #5
  call void @llvm.lifetime.start.p0(ptr nonnull %1) #5
  call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(12) %1, i8 -1, i64 12, i1 false), !tbaa !5
  %119 = getelementptr inbounds nuw i8, ptr %1, i64 4
  %120 = getelementptr inbounds nuw i8, ptr %1, i64 8
  br label %121

121:                                              ; preds = %193, %118
  %122 = phi i64 [ 0, %118 ], [ %194, %193 ]
  %123 = getelementptr inbounds nuw i32, ptr %1, i64 %122
  %124 = load i32, ptr %123, align 4, !tbaa !5
  %125 = icmp eq i32 %124, -1
  br i1 %125, label %126, label %193

126:                                              ; preds = %121
  store i32 0, ptr %123, align 4, !tbaa !5
  call void @llvm.lifetime.start.p0(ptr nonnull %2) #5
  %127 = trunc nuw nsw i64 %122 to i32
  store i32 %127, ptr %2, align 16, !tbaa !5
  %128 = load i32, ptr %1, align 16
  %129 = load i32, ptr %119, align 4
  %130 = load i32, ptr %120, align 8
  br label %132

131:                                              ; preds = %188
  call void @llvm.lifetime.end.p0(ptr nonnull %2) #5
  br label %193

132:                                              ; preds = %188, %126
  %133 = phi i32 [ %130, %126 ], [ %189, %188 ]
  %134 = phi i32 [ %129, %126 ], [ %173, %188 ]
  %135 = phi i32 [ %128, %126 ], [ %157, %188 ]
  %136 = phi i64 [ 0, %126 ], [ %138, %188 ]
  %137 = phi i32 [ 1, %126 ], [ %190, %188 ]
  %138 = add nuw nsw i64 %136, 1
  %139 = getelementptr inbounds nuw i32, ptr %2, i64 %136
  %140 = load i32, ptr %139, align 4, !tbaa !5
  %141 = sext i32 %140 to i64
  %142 = getelementptr inbounds [100 x i32], ptr %6, i64 %141
  %143 = getelementptr inbounds i32, ptr %1, i64 %141
  %144 = load i32, ptr %142, align 16, !tbaa !5
  %145 = icmp eq i32 %144, 0
  br i1 %145, label %156, label %146

146:                                              ; preds = %132
  %147 = icmp eq i32 %135, -1
  %148 = load i32, ptr %143, align 4, !tbaa !5
  br i1 %147, label %149, label %154

149:                                              ; preds = %146
  %150 = xor i32 %148, 1
  store i32 %150, ptr %1, align 16, !tbaa !5
  %151 = add nsw i32 %137, 1
  %152 = sext i32 %137 to i64
  %153 = getelementptr inbounds i32, ptr %2, i64 %152
  store i32 0, ptr %153, align 4, !tbaa !5
  br label %156

154:                                              ; preds = %146
  %155 = icmp eq i32 %135, %148
  br i1 %155, label %197, label %156

156:                                              ; preds = %154, %149, %132
  %157 = phi i32 [ %150, %149 ], [ %135, %154 ], [ %135, %132 ]
  %158 = phi i32 [ %151, %149 ], [ %137, %154 ], [ %137, %132 ]
  %159 = getelementptr inbounds nuw i8, ptr %142, i64 4
  %160 = load i32, ptr %159, align 4, !tbaa !5
  %161 = icmp eq i32 %160, 0
  br i1 %161, label %172, label %162

162:                                              ; preds = %156
  %163 = icmp eq i32 %134, -1
  %164 = load i32, ptr %143, align 4, !tbaa !5
  br i1 %163, label %167, label %165

165:                                              ; preds = %162
  %166 = icmp eq i32 %134, %164
  br i1 %166, label %197, label %172

167:                                              ; preds = %162
  %168 = xor i32 %164, 1
  store i32 %168, ptr %119, align 4, !tbaa !5
  %169 = add nsw i32 %158, 1
  %170 = sext i32 %158 to i64
  %171 = getelementptr inbounds i32, ptr %2, i64 %170
  store i32 1, ptr %171, align 4, !tbaa !5
  br label %172

172:                                              ; preds = %167, %165, %156
  %173 = phi i32 [ %168, %167 ], [ %134, %165 ], [ %134, %156 ]
  %174 = phi i32 [ %169, %167 ], [ %158, %165 ], [ %158, %156 ]
  %175 = getelementptr inbounds nuw i8, ptr %142, i64 8
  %176 = load i32, ptr %175, align 8, !tbaa !5
  %177 = icmp eq i32 %176, 0
  br i1 %177, label %188, label %178

178:                                              ; preds = %172
  %179 = icmp eq i32 %133, -1
  %180 = load i32, ptr %143, align 4, !tbaa !5
  br i1 %179, label %183, label %181

181:                                              ; preds = %178
  %182 = icmp eq i32 %133, %180
  br i1 %182, label %197, label %188

183:                                              ; preds = %178
  %184 = xor i32 %180, 1
  store i32 %184, ptr %120, align 8, !tbaa !5
  %185 = add nsw i32 %174, 1
  %186 = sext i32 %174 to i64
  %187 = getelementptr inbounds i32, ptr %2, i64 %186
  store i32 2, ptr %187, align 4, !tbaa !5
  br label %188

188:                                              ; preds = %183, %181, %172
  %189 = phi i32 [ %184, %183 ], [ %133, %181 ], [ %133, %172 ]
  %190 = phi i32 [ %185, %183 ], [ %174, %181 ], [ %174, %172 ]
  %191 = sext i32 %190 to i64
  %192 = icmp slt i64 %138, %191
  br i1 %192, label %132, label %131

193:                                              ; preds = %131, %121
  %194 = add nuw nsw i64 %122, 1
  %195 = icmp eq i64 %194, 3
  br i1 %195, label %196, label %121, !llvm.loop !11

196:                                              ; preds = %193
  call void @llvm.lifetime.end.p0(ptr nonnull %1) #5
  br label %198

197:                                              ; preds = %181, %165, %154
  call void @llvm.lifetime.end.p0(ptr nonnull %2) #5
  call void @llvm.lifetime.end.p0(ptr nonnull %1) #5
  br label %198

198:                                              ; preds = %197, %196, %117
  %199 = phi ptr [ @str.3, %197 ], [ @str.4, %196 ], [ @str, %117 ]
  %200 = phi i32 [ 0, %197 ], [ 1, %196 ], [ 1, %117 ]
  %201 = tail call i32 @puts(ptr nonnull dereferenceable(1) %199)
  call void @llvm.lifetime.end.p0(ptr nonnull %6) #5
  call void @llvm.lifetime.end.p0(ptr nonnull %5) #5
  ret i32 %200
}

; Function Attrs: mustprogress nocallback nofree nounwind willreturn memory(argmem: write)
declare void @llvm.memset.p0.i64(ptr writeonly captures(none), i8, i64, i1 immarg) #3

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #4

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(argmem: read) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite) }
attributes #2 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { mustprogress nocallback nofree nounwind willreturn memory(argmem: write) }
attributes #4 = { nofree nounwind }
attributes #5 = { nounwind }

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
